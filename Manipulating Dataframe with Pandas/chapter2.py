############### Pandas data structure
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




