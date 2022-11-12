import pandas as pd

df = pd.read_csv('mlb_players.csv')
df['Height'] = df['Height(inches)'] * 2.54
df['Weight'] = df['Weight(lbs)'] * 0.453592
print(df.loc[:9, ['Name', 'Height', 'Weight']])
