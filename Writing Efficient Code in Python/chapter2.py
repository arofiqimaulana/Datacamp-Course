################################# Examining Runtime #######################################
# using %timeit, %lsmagic
# number of runs = how many iteration you'd like to use to estimated the runtime 
# number of loops = how many times to you'd like to code to be exceuted per run

# ns = nanosecond	(10^-9)
# µs (us) =	microsecond	(10^-6)
# ms =	millisecond	(10^-3)
# s	= second (10^0)

# list : list() :	[]
# dictionary :	dict() : {}
# tuple : tuple() :	()

import numpy as np
rand_numb = np.random.rand(1000)

# examingin runtime
%timeit rand_numb = np.random.rand(1000)

# set number of runs to 2, number of loops to 10
%timeit -r2 -n10 rand_numb = np.random.rand(1000)

# multiple line
%% timeit 
numbs = []
for x in range(10):
    numbs.append(x)

# saving output (-o)
times = %timeit -o rand_numb = np.random.rand(1000)

# times for each run
times.timings

# best times
times.best

# worst times
times.worst


##################################### Task 1 (list comprehension or unpacking the range object into a list is faster)
# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*(range(51))]
print(nums_unpack)

%timeit nums_list_comp

%timeit nums_unpack


################################## Task 2 (Using %timeit: specifying number of runs and loops)
%timeit -r5 -n25 set(heroes)

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

################################## Task 2 (Using cell magic mode (%%timeit))

%%timeit 
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)

%%timeit 
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462

################################## Code Profiling Runtime ################################
import line_profiler

heroes = ['Batman','Superman','Wonder Woman']

hts = np.array([188.0, 191.0, 183.0])
wts = np.array([95.0, 101.0, 74.0])

def convert_units(heroes,heights,weights):

    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i],new_wts[i])
    
    return hero_data

%timeit convert_units(heroes,hts,wts) #only provide total runtime not line by line

# Using code profiling
%load_ext line_profiler
%lprun -f convert_units

############################## Task 1 (Using %lprun: spot bottlenecks)

def convert_units(heroes, heights, weights):

    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

%load_ext line_profiler
%lprun -f convert_units convert_units(heroes, hts, wts)

############################# Task 2 (Using %lprun: fix the bottleneck)

def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

%load_ext line_profiler
%lprun -f convert_units_broadcast convert_units_broadcast(heroes,hts,wts)

############################ Code Profiling for Memory Usage ################################
import sys

numb_list = [*range(1000)]
sys.getsizeof(num_list)

import numpy as np

nump_np = np.array(range(1000))
sys.getsizeof(nump_np)

# using memory profiling
# Only can be used on function in pysiical file (then we import it)
import memory_profiler
from hero_funct import convert_units

%load_ext memory_profiler
%mprun -f convert_units convert_units(heroes,hts,wts)


############################### Task 1 (Using %mprun: Hero BMI)

def calc_bmi_lists(sample_indices, hts, wts):

    # Gather sample heights and weights as lists
    s_hts = [hts[i] for i in sample_indices]
    s_wts = [wts[i] for i in sample_indices]

    # Convert heights from cm to m and square with list comprehension
    s_hts_m_sqr = [(ht / 100) ** 2 for ht in s_hts]

    # Calculate BMIs as a list with list comprehension
    bmis = [s_wts[i] / s_hts_m_sqr[i] for i in range(len(sample_indices))]

    return bmis

import memory_profiler
from bmi_lists import calc_bmi_lists
%load_ext memory_profiler
%mprun -f calc_bmi_lists calc_bmi_lists(sample_indices,hts,wts)

############################### Task 2 (Using %mprun: Hero BMI 2.0)

def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis

import memory_profiler
from bmi_arrays import calc_bmi_arrays
%load_ext memory_profiler
%mprun -f calc_bmi_arrays calc_bmi_arrays(sample_indices,hts,wts)

############################### Task 3 (Bringing it all together: Star Wars profiling)

def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes

def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes

# Use get_publisher_heroes() to gather Star Wars heroes
star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))

# Runtime
import line_profiler
%load_ext line_profiler
%lprun -f get_publisher_heroes get_publisher_heroes(heroes,publishers,'George Lucas')
%lprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes,publishers,'George Lucas')

# Memory Consumption
import memory_profiler
%load_ext memory_profiler
from hero_funcs import get_publisher_heroes
from hero_funcs import get_publisher_heroes_np

%mprun -f get_publisher_heroes get_publisher_heroes(heroes,publishers,'George Lucas')
%mprun -f get_publisher_heroes_np get_publisher_heroes_np(heroes,publishers,'George Lucas')

