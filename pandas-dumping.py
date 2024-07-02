import pandas as pd

df = pd.read_csv('england-premier-league-players-2018-to-2019-stats.csv')

print(df) #shows just a snippet

 # will print whole csv
# print(df.to_string())
print(df.head(12))
print()
print(df.tail(12))

#rows and columns of data frame
df.shape()
print(df.count())


print(df['full_name'])

print(df.loc['full_name'])
print(df[['full_name', 'Current Club']])

print(df.loc[df['Current Club'] == 'Arsenal, 'full_name'])

# while loc locates rows by lable, iloc locates by index or integer
print(df.iloc[1]) # first row

#second argument can be a list of columns to retreive
print(df.iloc[0, [0,3]]) #display first row, only 0 and 4th columns

df = df.set_index('full_name')

print(df.loc["Adam Smith"])

df.reset_index()

# in pandas, ~ means ! , | means or, & means and
print(df.loc[(df["Age"] < 25)] & df['position'] == 'defender', ['full_name'])

# altering the rows
df.loc[df['full_name' == 'Harry Kane', 'Current Club'] = 'Spurs'
print('''
Tottenham Hotsupur -> Spurs\n''', df)

# info about columns
print(df.columns())
