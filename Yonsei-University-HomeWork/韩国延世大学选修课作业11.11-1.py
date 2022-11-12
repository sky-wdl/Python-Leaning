import pandas as pd

df = pd.read_csv('doge.csv')

df['ma2'] = df['close'].rolling(window=2).mean()
df['ma3'] = df['close'].rolling(window=3).mean()
df['ma4'] = df['close'].rolling(window=4).mean()

# No edit
print(df['ma2'][10])
print(df['ma3'][12])
print(df['ma4'][4])
print(df.head())
