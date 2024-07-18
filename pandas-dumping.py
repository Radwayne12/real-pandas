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

#apply(fun) applies a function to a seiries (can be df)
print(df['full_name'].apply(lower))
 
print(df['full_name'].apply(lambda x: x.title()))

#apply to df
df.apply(len) # it will apply len to columns of df, not really used for it

# applymap(fun) can be used to apply fun to all cells
df.loc[1 == 1, ['full_name', 'Current Club]].applyman(len)

#map can change cells with respective values
df['full_name'].map({'Hary Kane': 'Haaary Kain', 'Harry Maguire': 'goat'})

# all the values that are not affected by map() will turn to NaN

# to leave other values as they are, replace() can be used instead of map()

df['Current Club'].replace({'Tottenham': 'Spurs', 'Manchester City':'Man City'})
#other values in the column will not be NaN

# to add a column
df['first_name'] = df['full_name'].split[0]

