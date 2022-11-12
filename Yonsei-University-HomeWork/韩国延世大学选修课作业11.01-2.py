import pandas as pd


def BMI(weight, height):
    return weight / (height * height)


df = pd.read_csv('mlb_players.csv', index_col='Name')
df['Height'] = df['Height(inches)'] * 2.54
df['Weight'] = df['Weight(lbs)'] * 0.453592
df['BMI'] = BMI(df["Weight"], df["Height"] * 0.01)
print(df.loc[["Paul Bako", "Chris Gomez"], ['Height', 'Weight', 'BMI']])

