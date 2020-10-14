############# Package
import pandas as pd
df = pd.read_csv('Sales.csv')
election = pd.read_csv('election.csv')


############# Indexing
# Indexing Using Square Brackets
df['salt']['Jan']

# Using Columns Atribut and Row Label
df.egg['Mar']

# using the .loc accesor
df.loc['May','Spam']

# using the iloc accesor
df.iloc[4,2]


#########################  Slicing DataFrame #########################
df['egg'][1:4] # Part of egg columns
df['egg'][4] # Associate with May
df.loc[:,'egg':'salt'] # All Rows Some Columns
df.loc['Jan' : 'Apr',:] # Some Rows All Columns
df.loc['Jan' : 'Apr',:'egg':'salt'] # Some Rows Some Columns
df.iloc[2:5,1]

df['Age'] # type Series
df[['Age']] # type DataFrame


############ Task
# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election.loc['Perry':'Potter',]

# Print the p_counties DataFrame
print(p_counties)

# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election.loc['Potter':'Perry':-1,]


# Print the p_counties_rev DataFrame
print(p_counties_rev)

############## Task
# Slice the columns from the starting column to 'Obama': left_columns
left_columns = election.loc[:,:'Obama']

# Print the output of left_columns.head()
print(left_columns.head())

# Slice the columns from 'Obama' to 'winner': middle_columns
middle_columns = election.loc[:,'Obama':'winner']

# Print the output of middle_columns.head()
print(middle_columns.head())

# Slice the columns from 'Romney' to the end: 'right_columns'
right_columns = election.loc[:,'Romney':]

# Print the output of right_columns.head()
print(right_columns.head())


############## Task
# Create the list of row labels: rows
rows = ['Philadelphia', 'Centre', 'Fulton']

# Create the list of column labels: cols
cols = ['winner','Obama','Romney']

# Create the new DataFrame: three_counties
three_counties = election.loc[rows,cols]

# Print the three_counties DataFrame

print(three_counties)


################## Filtering DataFrame ############################
df.salt > 60 # creating a boolean series
df[df.salt > 60]

enough_salt_sold  = df.salt > 60
df[enough_salt_sold]

# combining Filter
df[(df.salt > 30) & (df.salt <=200)] #Both Condition
df[(df.salt > 30) & (df.salt <=200)] #Either Condition

df.loc[:,df.all()] # select column with all nonzeroes
df.loc[:,df.isnull().any()] # select comuns with any NaNs
df.loc[:,df.notnull().any()] # select comuns with Non any NaNs

df.egg[df.salt > 55] += 5 # add 5 for suitable condition

################# Task 1
# Create the boolean array: high_turnout
high_turnout = election['turnout'] > 70

# Filter the election DataFrame with the high_turnout array: high_turnout_df
high_turnout_df = election[high_turnout]

# Print the high_turnout_results DataFrame
print(high_turnout_df)


################# Task 2
# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election['margin'] < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election.loc[too_close, 'winner'] = np.nan

# Print the output of election.info()
print(election.info())


################# Task 3
# Select the 'age' and 'cabin' columns: df
titanic = pd.read_csv('titanic.csv')
df = titanic[['age','cabin']]

# Print the shape of df
print(df.shape)

# Drop rows in df with how='any' and print the shape
print(df.dropna(how='any').shape)

# Drop rows in df with how='all' and print the shape
print(df.dropna(how='all').shape)

# Drop columns in titanic with less than 1000 non-missing values
print(titanic.dropna(thresh=1000, axis='columns').info())


################## Transorming DataFrame ############################
df.floordiv(12) # Convert to dozein units

def dozen(n):
    return n // 12

df.apply(lambda n: n // 12)

df['dozens_of_egg'] = df.egg.floordiv(12)

df.index = df.index.str.upper()
df.index = df.index.map(str.lower)

df['salty_egg'] = df.salt + df.dozens_of_egg


################### Task
# Write a function to convert degrees Fahrenheit to degrees Celsius: to_celsius
def to_celsius(F):
    return 5/9*(F - 32)

# Apply the function over 'Mean TemperatureF' and 'Mean Dew PointF': df_celsius
df_celsius = weather[['Mean TemperatureF','Mean Dew PointF']].apply(to_celsius)

# Reassign the column labels of df_celsius
df_celsius.columns = ['Mean TemperatureC', 'Mean Dew PointC']

# Print the output of df_celsius.head()
print(df_celsius.head())


################### Task
# Create the dictionary: red_vs_blue
red_vs_blue = {'Obama':'blue','Romney':'red'}

# Use the dictionary to map the 'winner' column to the new column: election['color']
election['color'] = election['winner'].map(red_vs_blue)

# Print the output of election.head()
print(election.head())


################### Task
# Import zscore from scipy.stats
from scipy.stats import zscore

# Call zscore with election['turnout'] as input: turnout_zscore
turnout_zscore = zscore(election['turnout'])

# Print the type of turnout_zscore
print(type(turnout_zscore))

# Assign turnout_zscore to a new column: election['turnout_zscore']
election['turnout_zscore'] = turnout_zscore

# Print the output of election.head()
print(election.head())

