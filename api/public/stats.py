from bfxapi import Client, PUB_REST_HOST

bfx = Client(rest_host=PUB_REST_HOST)


def get_stats(key: str, timeframe: str, symbol: str, side: str, section: str):
    resource = f"{key}:{timeframe}:{symbol}:{side}"
    if section == "last":
        data = bfx.rest.public.get_stats_last(resource)
    else:
        data = bfx.rest.public.get_stats_hist(resource)
    return data
