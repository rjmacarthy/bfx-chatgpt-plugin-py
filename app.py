import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from api.public.candles import get_candles
from api.public.tickers import get_tickers, get_t_ticker
from api.public.stats import get_stats
from api.public.book import get_t_book
from indicators.indicators import get_indicators

app = Flask(__name__)


CORS(
    app,
    origins=[
        f"https://chatgpt-bitfinex-plugin.azurewebsites.net",
        "https://chat.openai.com",
    ],
)

@app.route("/")
def index():
    return "Welcome to the Unofficial Bitfinex ChatGPT plugin"


@app.route("/tickers")
def tickers():
    symbols = request.args.get("symbols") or []
    symbols = symbols.split(",") if isinstance(symbols, str) else symbols
    return jsonify(get_tickers(symbols)), 200


@app.route("/stats")
def stats():
    key = request.args.get("key") or "pos.size"
    timeframe = request.args.get("timeframe") or "1m"
    symbol = request.args.get("symbol") or "fUSD"
    side = request.args.get("side") or "long"
    section = request.args.get("section") or "last"
    return jsonify(get_stats(key, timeframe, symbol, side, section)), 200


@app.route("/candles")
def candles():
    symbol = request.args.get("symbol") or "tBTCUSD"
    timeframe = request.args.get("timeframe") or "1h"
    return jsonify(get_candles(symbol, timeframe)), 200


@app.route("/book")
def book():
    symbol = request.args.get("symbol") or "tBTCUSD"
    precision = request.args.get("precision", "P0")
    return jsonify(get_t_book(symbol, precision)), 200  # type: ignore


@app.route("/analysis")
def analysis():
    symbol = request.args.get("symbol") or "tBTCUSD"
    timeframe = request.args.get("timeframe") or "1h"
    candle_data = get_candles(symbol, timeframe)
    data = get_indicators(candle_data)
    return jsonify(data), 200


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
    app.run()
