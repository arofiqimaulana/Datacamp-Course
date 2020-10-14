############### Pandas data structure ########################
### Index : sequence of label
### Series : 1D array with index
### DataFrame : 2D array with Series as columns

############### Creating Series 
import pandas as pd
prices = [10.7, 10.8, 10.74, 10.71, 10.79]
shares = pd.Series(prices)
print(shares)

############### Creating Index
### Index are immutable
days = ['Mon','Tue','Wed','Thur','Fri']
shares = pd.Series(days,index=days)
shares.index.nam = 'Week' # modifying index name
print(shares)

unemployment = pd.read_csv('Unemployment.csv',index='ZIP')

############### Task 1
cubes = [i**3 for i in range(10)] 

# Equivalence with

cubes = []
for i in range(10):
    cubes.append(i**3)

# Create the list of new indexes: new_idx
new_idx = [k.upper() for k in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)

############### Task 2

sales = pd.read_csv('sales.csv')

# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(sales)

################ Task 3
# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)


################# Hierarchical Indexing ##################
import pandas as pd
stocks = pd.read_csv('dataset/stocks.csv')

# Setting Index
stocks = stocks.set_index(['Symbol','Date']) # Index is no longer range of int

# Sorting Index
stocks = stocks.sort_index()

# Indexing
stocks.loc[('CSCO','2016-01-01')]

stocks.loc[('CSCO','2016-01-01'),'Volume']

# Slicing
stocks.loc['AAPL'] # outermost index

stocks.loc['AAPL':'CSCO'] # outermost index

stocks.loc[(['AAPL , CSCO'],'2016-01-01'),:] # fancy indexing

stocks.loc[(['AAPL , CSCO'],'2016-01-01'), 'Close'] # fancy indexing

stocks.loc[('AAPL',['2016-01-01','2016-01-02']),:] # fancy indexing

stocks.loc[('AAPL',['2016-01-01','2016-01-02']),'Close'] # fancy indexing

stocks.loc[(slice(None),slice('2016-01-01','2016-01-03')),:]

################# Task 4
# Print sales.loc[['CA', 'TX']]
print(sales.loc[['CA','TX']])

# Print sales['CA':'TX']
print(sales['CA':'TX'])

# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state','month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)

################ Task 5

# Set the index to the column 'state': sales
sales = sales.set_index('state')

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])


################ Task 6

# Look up data for NY in month 1 in sales: NY_month1
NY_month1 = sales.loc[('NY',1)]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA','TX'],2),:]

# Access the inner month index and look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None),2),:]


