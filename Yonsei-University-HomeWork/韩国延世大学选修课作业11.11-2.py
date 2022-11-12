import pandas as pd
import numpy as np

df = pd.read_csv('https://esohn.be/text/doge.csv')
df['bull'] = np.where(df['close'] > df['close'].mean(), 'True', 'False')
print(df[['close', 'bull']])
