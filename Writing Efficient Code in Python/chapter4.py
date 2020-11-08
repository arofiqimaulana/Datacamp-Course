############################## Pandas DataFrame Iteration ########################
import pandas as pd

baseball_df = pd.read_csv('baseball_stats.csv')

# calculating win percentage
import numpy as np

def cal_win_perc(wins, games_played):
    win_perc = wins/games_played

    return np.round(win_perc,2)

win_perc = cal_win_perc(50,100)

# Adding win percentage to dataframe
win_perc_list = []
for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]
    wins = row['W']
    games_played = row['G']
    win_perc = cal_win_perc(wins, games_played)
    win_perc_list.append(win_perc)

baseball_df['WP'] = win_perc_list

######### Second Method (Iterate using .iterrows)
win_perc_list = []

for i, row in baseball_df.iterrows():
    win = row['W']
    games_played = row['G']
    win_perc = cal_win_perc(wins, games_played)
    win_perc_list.append(win_perc)

baseball_df['WP'] = win_perc_list


################################# Task 1 (Iterating with .iterrows())

# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)

# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))

# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))

################################ Task 2 (Run differentials with .iterrows())

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)


############################### Iterate method : itertuple #############################

# first method
for row_tuple in team_win_df.iterrows():
    print(row_tuple)
    print(type(row_tuple[1]))

# second method
for row_named_tuple in team_win_df.itertuple():
    print(row_named_tuple)

print(row_named_tuple.index)
print(row_named_tuple.name)

############################## Task 1 (Iterating with .itertuples())

# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
  print(row)

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)

########################### Task 2 (Run differentials with .itertuples())

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

# Loop over the DataFrame and calculate each row's run differential
run_diffs = []

for row in yankees_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)

# In what year within your DataFrame did the New York Yankees have the highest run differential?
yankees_df[yankees_df.RD==yankees_df['RD'].max()]


############################# Pandas Alternatife to looping ###############################
# Takes a function and applies to dataframe
# Must specify with anonymous to apply (0 for columns, 1 for rows)

baseball_df.apply(
    lambda row : calc_run_diff(row['RS'],row['RA']),
    axis = 1
)

############################## Task 1 (Analyzing baseball stats with .apply())

def text_playoffs(num_playoffs): 
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No' 

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

############################# Task 2 (Settle a debate with .apply())

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])

############################ Optimal pandas iterating #########################
# Eliminating loops applied to using pandas as well (pandas is built in numpy)

wins_np = baseball_df.values # tipe datanya adalalah , so we can use the power of vectorisation
run_diffs_np = baseball_df['RS'].values - baseball_df['RA'].values
baseball_df['RD'] = run_diffs_np

############################ Task 1 (Replacing .iloc with underlying arrays)
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list

# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())

########################## Task 2 (Runtime)
%%timeit
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row['W']
    games_played = row['G']

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df['WP'] = win_percs_list

%%timeit
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

####################### Task 3 (Bringing it all together: Predict win percentage)
def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())