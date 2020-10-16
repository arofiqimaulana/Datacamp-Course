############################ Categorical & Group By ##########################
import pandas as pd 

sales = pd.DataFrame(
    {
        'weekday' : ['Sun','Sun','Mon','Mon'],
        'city' : ['Austin','Dallas','Austin','Dallas'],
        'bread' : [139,237,326,456],
        'butter' : [20,45,70,98]
    }
)

sales.groupby('weekday').count()

sales.groupby('weekday')['bread'].sum() 

sales.groupby('weekday')['bread','butter'].sum()

sales.groupby(['weekday','city']).mean() # groub by multi index

customers = pd.Series(['Dave','Alice','Bob','Alice'])

sales.groupby(customers)['bread'].sum() # use series before

sales['weekday'].unique()

sales['weekday'] = sales['weekday'].astype('category') # faster. less memory if we change to category


########################### Task 1
titanic = pd.read_csv('titanic.csv')

# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Aggregate 'survived' column of by_class by count
count_by_class = by_class['survived'].count()

# Print count_by_class
print(count_by_class)

# Group titanic by 'embarked' and 'pclass'
by_mult = titanic.groupby(['embarked','pclass'])

# Aggregate 'survived' column of by_mult by count
count_mult = by_mult['survived'].count()

# Print count_mult
print(count_mult)


############################# Task 2
# Read life_fname into a DataFrame: life
life = pd.read_csv(life_fname, index_col='Country')

# Read regions_fname into a DataFrame: regions
regions = pd.read_csv(regions_fname,index_col='Country')

# Group life by regions['region']: life_by_region
life_by_region = life.groupby(regions['region'])

# Print the mean over the '2010' column of life_by_region
print(life_by_region['2010'].mean())


############################# Custom Aggregation ##################################
sales.groupby('city')[['bread','butter']].agg(['max','sum']) # multiple aggregation

def data_range(series):
    return series.max() - series.min()

sales.groupby('city')[['bread','butter']].agg(data_range) #custom aggregation

sales.groupby(customers)[['bread','butter']].agg({
    'bread' : 'sum',
    'butter' :data_range
}) # different aggregation



############################ Task 1
# Group titanic by 'pclass': by_class
by_class = titanic.groupby('pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['age','fare']]

# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max','median'])

# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])

# Print the median fare in each class
print(aggregated.loc[:,('fare')]['median'])


########################### Task 2
# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder = pd.read_csv('gapminder.csv',index_col=['Year','region','Country']).sort_index()

# Group gapminder by 'Year' and 'region': by_year_region
by_year_region = gapminder.groupby(level=['Year','region'])

# Define the function to compute spread: spread
def spread(series):
    return series.max() - series.min()

# Create the dictionary: aggregator
aggregator = {'population':'sum', 'child_mortality':'mean', 'gdp':spread}

# Aggregate by_year_region using the dictionary: aggregated
aggregated = by_year_region.agg(aggregator)

# Print the last 6 entries of aggregated 
print(aggregated.tail(6))

########################## Task 3
# Read file: sales
sales = pd.read_csv('sales.csv',index_col='Date',parse_dates=True)

# Create a groupby object: by_day
by_day = sales.groupby(sales.index.strftime('%a'))

# Create sum: units_sum
units_sum = by_day['Units'].sum()

# Print units_sum
print(units_sum)


################################### Z Score ###########################
def zscore(series):
    return (series-series.mean())/series.std()

auto = pd.read_csv('auto-mgp.csv')
auto.head()

zscore(auto['mpg']).head() # mpg z score

auto.groupby('yr')['mpg'].transform(zscore).head() #MPG Zscore by year

# Apply transformation and aggregation

def zscore_with_year_and_name(group):
    df = pd.DataFrame(
        {
            'mpg' : zscore(group['mpg']),
            'year' : group['yr'],
            'name' : group['name']
        }
    )

    return df

auto.groupby('yr').apply(zscore_with_year_and_name).head()

################################## Task 1
# Import zscore
from scipy.stats import zscore

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby('region')['life','fertility'].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] >3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers]

# Print gm_outliers
print(gm_outliers)

################################# Task 2
# Create a groupby object: by_sex_class
by_sex_class = titanic.groupby(['sex','pclass'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age and assign to titanic['age']
titanic.age = by_sex_class['age'].transform(impute_median)

# Print the output of titanic.tail(10)
print(titanic.tail(10))

################################ Task 3
# Group gapminder_2010 by 'region': regional
regional = gapminder_2010.groupby('region')

# Apply the disparity function on regional: reg_disp
reg_disp = regional.apply(disparity)

# Print the disparity of 'United States', 'United Kingdom', and 'China'
print(reg_disp.loc[['United States','United Kingdom','China'],:])


############################## Group By Object ##################################
splitting = auto.groupby('yr')

for group_name, group in splitting:
    avg = group['mpg'].mean()
    print(group_name,avg)

for group_name, group in splitting:
    avg = group.loc[group['name'].str.contains('chevrolet'),'mpg'].mean()
    print(group_name,avg)

############################# Task 1
# Create a groupby object using titanic over the 'sex' column: by_sex
by_sex = titanic.groupby('sex')

# Call by_sex.apply with the function c_deck_survival
c_surv_by_sex = by_sex.apply(c_deck_survival)

# Print the survival rates
print(c_surv_by_sex)

############################ Task 2
# Read the CSV file into a DataFrame: sales
sales = pd.read_csv('sales.csv', index_col='Date', parse_dates=True)

# Group sales by 'Company': by_company
by_company = sales.groupby('Company')

# Compute the sum of the 'Units' of by_company: by_com_sum
by_com_sum = by_company['Units'].sum()
print(by_com_sum)

# Filter 'Units' where the sum is > 35: by_com_filt
by_com_filt = by_company.filter(lambda g:g['Units'].sum() > 35 )
print(by_com_filt)

########################### Task 3
# Create the Boolean Series: under10
under10 = (titanic['age'] < 10).map({True:'under 10', False:'over 10'})

# Group by under10 and compute the survival rate
survived_mean_1 = titanic.groupby(under10)['survived'].mean()
print(survived_mean_1)

# Group by under10 and pclass and compute the survival rate
survived_mean_2 = titanic.groupby([under10,'pclass'])['survived'].mean()
print(survived_mean_2)


############################ Task 4
# Select the 'NOC' column of medals: country_names
medals = pd.read_csv('medals.csv')
country_names = medals['NOC']

# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()

# Print top 15 countries ranked by medals
print(medal_counts.head(15))

############################ Task 5
# Construct the pivot table: counted
counted = medals.pivot_table(index='NOC',columns='Medal',values='Athlete',aggfunc='count')

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis='columns')

# Sort counted by the 'totals' column
counted = counted.sort_values('totals', ascending=False)

# Print the top 15 rows of counted
print(counted.head(15))

############################### Understaning the column labels #############################
############################# Task 1
# Select columns: ev_gen
ev_gen = medals[['Event_gender','Gender']]

# Drop duplicate pairs: ev_gen_uniques
ev_gen_uniques = ev_gen.drop_duplicates()

# Print ev_gen_uniques
print(ev_gen_uniques)

############################# Task 2
# Group medals by the two columns: medals_by_gender
medals_by_gender = medals.groupby(['Event_gender','Gender'])

# Create a DataFrame with a group count: medal_count_by_gender
medal_count_by_gender = medals_by_gender.count()

# Print medal_count_by_gender
print(medal_count_by_gender)

############################# Task 3
# Create the Boolean Series: sus
sus = (medals.Event_gender == 'W') & (medals.Gender=='Men')

# Create a DataFrame with the suspicious row: suspect
suspect = medals[sus]

# Print suspect
print(suspect)












