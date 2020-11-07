############################# Efficiently combining, counting, and iterating #######################
############### 1. Combining Objects
names = ['Bulbasaur','Charmander','Squirtle']
hps = [45, 39, 44]

# first method
combined = []

for i,pokemon in enumerate(names):
    combined.append((pokemon,hps[i]))

print(combined)

# second method
combined_zip = zip(names,hps)
combined_zip_list = [*combined_zip] # unpack

############### 2. Counting with loops
# Each pokemons'type (720 total)
poke_types = ['Grass', 'Dark', 'Fire', 'Fire']

# first method
type_counts = {}
for poke_type in poke_types:
    if poke_type not in type_counts:
        type_counts[poke_type] = 1
    else:
        type_counts[poke_type] += 1

# second method
from collections import Counter
type_counts = Counter(poke_types)

############### 3. Combinations with loops
poke_types = ['Bug', 'Fire','Ghost','Grass','Water']
combos = []

# first method
for x in poke_types:
    for y in poke_types:
        if x==y:
            continue
        if ((x,y) not in combos) & ((y,x) not in combos()):
            combos.append(x,y)

# second method
from itertools import combinations
combos_adj = combinations(poke_types,2)

################################ Task 1 (Combining Pokémon names and types)
# Combine names and primary_types
names_type1 = [*zip(names, primary_types)]

print(*names_type1[:5], sep='\n')

# Combine all three lists together
names_types = [*zip(names,primary_types,secondary_types)]

print(*names_types[:5], sep='\n')

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5],primary_types[:3])]

print(*differing_lengths, sep='\n')

################################# Task 2 (Counting Pokémon from a sample)
from collections import Counter
type_counts = Counter(poke_types)

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Use list comprehension to get each Pokémon's starting letter
starting_letters = [i[0] for i in names]

# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

############################### Task 3 (Combinations of Pokémon)
# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon,4)]
print(combos_4)

############################## Set Theory ####################################
# sets if faster than list or tuple

in_common = []
list_a = ['Bulbasaur', 'Charmander', 'Squirtle']
list_b = ['Caterpie','Pidgey','Squirtle']

# first method
for pokemon_a in list_a:
    for pokemon_b in list_b:
        if pokemon_a == pokemon_b:
            in_common.append(pokemon_a)

print(in_common)

# second method
set_a = set(list_a)
set_b = set(list_b)

set_a.intersection(set_b)
set_a.difference(set_b)
set_b.difference(set_a)
set_a.symmetric_difference(set_b) 
set_a.union(set_b)

# unique with sets
primary_types = ['Grass','Grass','Pshycic','Dark','Bug']

unique_types = []

# first method
for prim_type in primary_types:
    if prim_type not in unique_types:
        unique_types.append(prim_type)

# second method
unique_types_set = set(primary_types)

################################### Task 1 (Exercise : A taste of things to come)

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Print the list created using the Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)

################################### Task 2 (Comparing Pokédexes)
# Convert both lists to sets
ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)

################################ Task 3 (Searching for Pokémon)
# Convert Brock's Pokédex to a set
brock_pokedex_set = set(brock_pokedex)
print(brock_pokedex_set)

# Check if Psyduck is in Ash's list and Brock's set
print('Psyduck' in ash_pokedex)
print('Psyduck' in brock_pokedex_set)

# Check if Machop is in Ash's list and Brock's set
print('Machop' in ash_pokedex)
print('Machop' in brock_pokedex_set)

%timeit 'Psyduck' in ash_pokedex
%timeit 'Psyduck' in brock_pokedex_set

%timeit 'Machop' in ash_pokedex
%timeit 'Machop' in brock_pokedex_set

################################# Task 4 (Gathering unique Pokémon)
# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n') 

# Compare performance
def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques

%timeit find_unique_items(names)
%timeit uniq_names_set = set(names)

##################################### Eliminate Loops ################################
# Looping in python:
# 1. for
# 2. while 
# 3. nested 

############### Eliminating loops with built-in
poke_stats = [
    [90, 92, 75, 60],
    [25, 10, 15, 90],
    [65, 130, 60, 75]
]

# for loop approach
totals = []
for row in poke_stats:
    totals.append(sum(row))

# List Comprehension
total_comp = [sum(row) for row in poke_stats]

# Builts-in map() function
total_map = [*map(sum, poke_stats)]

############### Eliminating loops with numpy
# for loop approach
avgs = []
for row in poke_stats:
    avg = np.mean(row)
    avg.append(avgs)

avgs_np = poke_stats.mean(axis=1)

###################################### Task 1 (Gathering Pokémon without a loop)
# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen in (1,2)]

# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

##################################### Task 2 (Pokémon totals and averages without a loop)
# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

#################################### Writing the better loops ############################
### Moving Calculation above loop
### perintah yang statis,seharusnya tidak ditaruh di dalam loop

names = ['Absol', 'Aron', 'Jynx', 'Natu', 'Onix']
attacks = np.array([130, 70, 50, 50, 45])

# first method
for pokemon, attack in zip(names,attacks):
    total_attack_avg = attacks.mean() # it should be in outer
    if attack > total_attack_avg:
        print(
            "{}'s attack: {} > average {}!"
            .format(pokemon,attack,total_attack_avg)
        )

# second method
import numpy as np
total_attack_avg = attacks.mean()
for pokemon, attack in zip(names,attacks):
    if attack > total_attack_avg:
        print(
            "{}'s attack: {} > average {}!"
            .format(pokemon,attack,total_attack_avg)
        )

### Using Holistic Conversions
names = ['Pikachu', 'Squirtle', 'Articuno']
legend_status = [False, False, True]
generations = [1,1,1]

# first method
poke_data = []
for poke_tuple in zip(names,legend_status,generations):
    poke_list = list(poke_tuple)
    poke_data.append(poke_list)

# second method
poke_data_tuples []
for poke_tuple in zip(names,legend_status,generations):
    poke_data_tuples.append(poke_tuple)

poke_data = [*map(list,poke_data_tuples)]


################################ Task 1 (One-time calculation loop)