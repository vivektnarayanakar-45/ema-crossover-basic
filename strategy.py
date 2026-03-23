import pandas as pd

def ema_strategy(df):
    df['ema_9'] = df['close'].ewm(span=9).mean()
    df['ema_21'] = df['close'].ewm(span=21).mean()

    df['signal'] = 0
    df.loc[df['ema_9'] > df['ema_21'], 'signal'] = 1
    df.loc[df['ema_9'] < df['ema_21'], 'signal'] = -1

    return df
