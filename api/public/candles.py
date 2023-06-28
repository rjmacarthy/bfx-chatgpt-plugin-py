from bfxapi import Client, PUB_REST_HOST

bfx = Client(rest_host=PUB_REST_HOST)


def get_candles(symbol: str, timeframe):
    return bfx.rest.public.get_candles_hist(symbol=symbol, tf=timeframe)
