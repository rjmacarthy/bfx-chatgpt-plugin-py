from typing import List
from bfxapi import Client, PUB_REST_HOST

bfx = Client(rest_host=PUB_REST_HOST)


def get_tickers(symbols: List[str]):
    return bfx.rest.public.get_tickers(symbols=symbols)


def get_t_ticker(symbol: str):
    return bfx.rest.public.get_t_ticker(symbol=symbol)
