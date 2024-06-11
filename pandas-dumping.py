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


print(df['full_name'])

print(df.loc(df['full_name']))
