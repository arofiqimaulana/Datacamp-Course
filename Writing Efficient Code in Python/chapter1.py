################################# Writing Efficient Code #######################################
# # Efficient definition
# 1. Efisien has minimal completion time (fast runtime)
# 2. minimal resource consumption (small memory footprint)

# # Pythonic definition
# 1. Focus on readability
# 2. Using Python's construct as intended

# Non Pythonic
double_numbers = []
for i in range(len(numbers)):
    double_numbers.append(number[i]*2)

# Pythonic
double_numbers = [x*x for x in numbers]


################################# Task 1 (A taste of things to come)
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
 = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)

################################## Task 2 (Zen of Python)  
# In the video, we covered the Zen of Python written by Tim Peters, which lists 19 idioms that serve 
# as guiding principles for any Pythonista. Python has hundreds of Python Enhancement Proposals, 
# commonly referred to as PEPs (https://www.python.org/dev/peps/pep-0020/). The Zen of Python is one of these PEPs and is documented as PEP20.

# One little Easter Egg in Python is the ability to print the Zen of Python using the command import this. 
# Let's take a look at one of the idioms listed in these guiding principles.

################################## Task 2 (Built-in practice: range() )
# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(nums_list2)

################################ Task 3 (Built-in practice: enumerate() )
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)


############################### Task 4 (Built-in practice: map() )
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

names_uppercase = []

for name in names:
  names_uppercase.append(name.upper())

# Use map to apply str.upper to each element in names
names_map  = map(lambda x:x.upper(),names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)

############################# The Power of numpy array #################################
# a numpy array provide fast and memory efficient alternatife to list
# a numpy array a homogenious (contain one type only) 
# Python list doesnt support broadcasting

nump_np_ints = np.array([1,2,3])
nump_np_ints.dtype

# python list doesnt support broadcasting
nums = [-2,-1,0,1,2]
nums **2

# List approach
sqrd_nums = []
for num in num:
    sqrd_nums.append(num**2)

print(sqrd_nums)

# List Comprehention approach
sqrd_nums = [num ** 2 for num in nums]

# Numpy array approach
nump_ar = np.array(nums)
nump_ar ** 2


############################### Task 1 (Practice with NumPy arrays)
# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)

############################## Task 2 (Bringing it all together: Festivus!)
# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

