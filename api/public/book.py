from typing import Literal
from bfxapi import Client, PUB_REST_HOST

bfx = Client(rest_host=PUB_REST_HOST)


def get_t_book(symbol: str, precision: Literal["P0", "P1", "P2", "P3", "P4"]):
    return bfx.rest.public.get_t_book(pair=symbol, precision=precision)
