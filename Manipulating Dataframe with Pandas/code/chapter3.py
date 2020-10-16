#################### Pivoting Dataframes ##########################
import pandas as pd 
trials = pd.read_csv('trials01.csv')

trials.pivot(index='treatment', 
            columns='gender',
            values='responce')

trials.pivot(index='treatment',columns='gender') #pivotting multiple index


#################### Task 1
users = pd.read_csv('users01.csv')

# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index='weekday',columns='city',values='visitors')

# Print the pivoted DataFrame
print(visitors_pivot)


#################### Task 2
# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index='weekday',columns='city',values='signups')

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index='weekday',columns='city')

# Print the pivoted DataFrame
print(pivot)


######################### Stacking and Unstacking Dataframes #######################

trials = trials.set_index(['treatment','gender']) # creating multiple index

trials.unstack(level='gender') # Equivalence with
trials.unstack(level=1) # 0 = 'treatment', 1='gender'

# Stacking Dataframes
trials_by_gender = trials.stack(level='gender')

# Swapping level
swapped = stacked.swaplevel(0,1)

# Sorting index
sorted_trials = swapped.sort_index()


######################### Task 1
# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level='weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))


########################## Task 2
# Unstack users by 'city': bycity
bycity = users.unstack(level='city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))

########################## Task 3
# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level='city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0,1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))


############################# Melting Dataframes ############################
# restore a pivoted DataFrame to its original form
# change stack to original dataframes so the index now are gone

new_trials = pd.read_csv('new_trials01.csv')
pd.melt(new_trials)

pd.melt(new_trials,id_vars=['treatment'],value_var=['F','M']) # specifying id_vars
pd.melt(new_trials,id_vars=['treatment'],var_name='gender',value_name='responce') #specifiying value names

############################# Task 1
# Reset the index: visitors_by_city_weekday
visitors_by_city_weekday =  visitors_by_city_weekday.reset_index()

# Print visitors_by_city_weekday
print(visitors_by_city_weekday)

# Melt visitors_by_city_weekday: visitors
visitors = pd.melt(visitors_by_city_weekday, id_vars=['weekday'], value_name='visitors')

# Print visitors
print(visitors)


############################## Task 2
# Melt users: skinny
skinny = pd.melt(users,id_vars=['weekday','city'],value_vars=['visitors','signups'])

# Print skinny
print(skinny)


############################# Task 3
# Set the new index: users_idx
users_idx = users.set_index(['city','weekday'])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = pd.melt(users_idx,col_level=0)

# Print the key-value pairs
print(kv_pairs)

############################# Pivot Tables ###################################
trials.pivot_table(index='treatment',
                    columns ='gender',
                    values='response',
                    aggfunc='count')

############################# Task 1
# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = users.pivot_table(index='weekday',columns='city')

# Print by_city_day
print(by_city_day)

############################# Task 1
# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = users.pivot_table(index='weekday',aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = users.pivot_table(index='weekday',aggfunc=len)

# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))

############################# Task 2
# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = users.pivot_table(index='weekday',aggfunc='sum')

# Print signups_and_visitors
print(signups_and_visitors)

# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = users.pivot_table(index='weekday',aggfunc='sum',margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)







