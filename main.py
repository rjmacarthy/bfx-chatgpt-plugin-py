import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from api.public.candles import get_candles
from api.public.tickers import get_tickers, get_t_ticker
from api.public.stats import get_stats
from api.public.book import get_t_book

app = Flask(__name__)

PORT = 3333

CORS(app, origins=[f"http://localhost:{PORT}", "https://chat.openai.com"])


@app.route("/tickers")
def tickers():
    symbols = request.args.get("symbols") or []
    symbols = symbols.split(",") if isinstance(symbols, str) else symbols
    return jsonify(get_tickers(symbols)), 200


@app.route("/stats/<key>/<timeframe>/<symbol>/<side>/<section>")
def stats():
    key = request.args.get("key") or "funding.size"
    timeframe = request.args.get("timeframe") or "1m"
    symbol = request.args.get("symbol") or "fUSD"
    side = request.args.get("side") or "long"
    section = request.args.get("section") or "last"
    return jsonify(get_stats(key, timeframe, symbol, side, section)), 200


@app.route("/candles")
def candles():
    symbol = request.args.get("symbol") or "tBTCUSD"
    return jsonify(get_candles(symbol)), 200


@app.route("/book")
def book():
    symbol = request.args.get("symbol") or "tBTCUSD"
    precision = request.args.get("precision", "P0")
    return jsonify(get_t_book(symbol, precision)), 200  # type: ignore


@app.route("/analysis")
def analysis():
    symbol = request.args.get("symbol") or "tBTCUSD"
    candle_data = get_candles(symbol)
    ticker = get_t_ticker(symbol)
    return jsonify({"candles": candle_data, "ticker": ticker}), 200


@app.route("/.well-known/ai-plugin.json")
def serve_manifest():
    return send_from_directory(os.path.dirname(__file__), "manifest/ai-plugin.json")


@app.route("/openapi.json")
def serve_openapi_json():
    return send_from_directory(os.path.dirname(__file__), "manifest/openapi.json")


@app.route("/ai-plugin.json")
def serve_ai_json():
    return send_from_directory(os.path.dirname(__file__), "manifest/openapi.json")


if __name__ == "__main__":
    app.run(port=PORT)
