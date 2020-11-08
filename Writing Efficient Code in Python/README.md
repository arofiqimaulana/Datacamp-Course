# Writing Efficient Code in Python

## 1. Efficient definition
1. Efisien has minimal completion time (fast runtime)
2. minimal resource consumption (small memory footprint)

## 2. Pythonic definition
1. Focus on readability
2. Using Python's construct as intended

```
# Non Pythonic
double_numbers = []
for i in range(len(numbers)):
    double_numbers.append(number[i]*2)

# Pythonic
double_numbers = [x*x for x in numbers]
```

## 3. Built-ins
1. Bulit-in types
- list, tuple, set, dict and others

2. Built-in function
- print(), len(), range(), round(), enumerate(), map(), zip(), and others

3. Built-in modules
- os, sys, itertools, collections, math and others

## 4. The Power of Numpy Array
- a numpy array provide fast and memory efficient alternatife to list
- a numpy array a homogenious (contain one type only) 
- Python list doesnt support broadcasting (broadcasting refers to ability to vectorize operations)
- has advantages in indexing capability
- also has boolean indexing 
- A numpy array supports boolean indexing and has much better one-dimensional indexing capabilities.

## 5. Measuring runtime
```
# one line
%timeit rand_numb = np.random.rand(1000)

# multiple line
%% timeit 

# set number of runs to 2, number of loops to 10
%timeit -r2 -n10 rand_numb = np.random.rand(1000)

# saving output (-o)
times = %timeit -o rand_numb = np.random.rand(1000)

```

## 6. Examining Runtime & Memory Usage 
```
# Examining Runtime
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
```

## 7. Writing Better Loops
1. Moving Calculation above loop (Mengeluarkan perintah statis yang ada di dalam looping)
2. Using Holistic Conversion (map, unpack, list comprehention)

## Theoritical Conclusion
- using .iterrows is faster than .iloc (when iterate a dataframe)
- Use list comprehension is faster than for loop
- Efficient in combining object can we get by unpack zip
- Efficient in counting object can we get by using package (from collections import Counter)
- Efficient in combining object can we get by using package (from itertools import combinations)
- sets if faster than list or tuple
- Eliminating loops with built-in is faster than traditional for loops (enumerate, map, unpacked, list comprehention)
- a numpy array provide fast and memory efficient alternatife to list
- itertuples is faster than iterrows
- avoid using loop if you can go without loop (example : loop in pandas can be replaced by )
- Calculate the win percentage predictions using NumPy arrays is fastest, followed by Use a loop and .itertuples() to collect each row's predicted win percentage, and followed by Apply predict_win_perc to each row of the DataFrame