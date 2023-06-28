import pandas as pd
import pandas_ta as ta

def get_indicators(candles):
    df = pd.DataFrame(candles)
    macd = df.ta.macd().dropna()
    rsi = df.ta.rsi().dropna()
    df = pd.concat([macd, rsi], axis=1)
    return df.to_dict(orient="records")
