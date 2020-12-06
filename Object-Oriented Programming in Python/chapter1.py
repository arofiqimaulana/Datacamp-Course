#################################### Procedural Programming VS Object-Oriented Programming #########################################
######## Procedural Programming :
# 1. Code as sequence of steps
# 2. Great for data analysis and scripts

######## Object-Oriented Programming
# 1. Code is interactions of objects
# 2. Great for building frameworks and tools

############################# Q1 ##################################
# Objects and Class are different terms describing the same concept. (FALSE)

# Concepts of object and class are related, but have a fundamental difference: 
# an object is a particular representation of a class, while a class is just an abstract pattern.

############################# Q2 ####################################
# Encapsulation is a software design practice of bundling the data
# and the methods that operate on that data. (TRUE)

############################# Q3 ####################################
# Atributes encode the state of an object and represented by variables. (TRUE) 

############################# Q4 #####################################
# Methods encode behaviour of an object and represented by functions. (TRUE)

############################# Q5 #####################################
# .column is an example of a method of a DataFrame Object. (FALSE)

############################# Q6 #####################################
# Object is an abstract template describing the general states and behaviours. (FALSE) 

############################# Q7 ####################################
# A programming languages can be either object-oriented or procedural but not both. (FALSE)


######################################### Task 2 (Exploring object interface)
type(mystery) # __main__.Employee

# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)

######################################## Class Anatomy : Atributes and Methods ##########################
# Classes are templates, how to refer data of a particular object ?
# self is a standard-in for a particular object used in class definition
# should be the first argument of any method



###################################### Task 1 (Understanding class definitions)
# Objects and classes consist of attributes (storing the state) and methods (storing the behavior).
# Before you get to writing your own classes, you need to understand the basic structure of the class, and 
# how attributes in the class definition relate to attributes in the object. In this exercise, 
# you have a class with one method and one attribute, as well as the object of that class.

class MyCounter:
    def set_count(self,n):
        self.count = n

mc = MyCounter()
mc.set_count(5)
mc.set_count = mc.count + 1
print(mc.count)

##################################### Task 2 (Create your first class)

# Create an empty class Employee
class Employee:
    pass

# Create an object emp of class Employee 
emp = Employee()

# Include a set_name method
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Print the name of emp
print(emp.name)

class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method
  def set_salary(self,new_salary):
    self.salary = new_salary
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

#################################### Task 2 (Using attributes in class definition)
#### Sub Task 1
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 
  
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)

#### Sub Task 2
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self,amount):
        self.salary = self.salary + amount

emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.salary)
emp.give_raise(1500)
print(emp.salary)

#### Sub Task 3
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary/12

    
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)

####################################### __Init__ contructtor ###########################
# __init__ constructor memperbolehkan kita menulis 2 buah parameter dalam satu fungsi


###################################### Task 1 (Add a class constructor)
### Sub Task 1
class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
    
    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)     

### Sub Task 2 
class Employee:
  
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        self.salary = salary

        if self.salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")
   
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

### Sub Task 3 
# Import datetime from datetime
from datetime import datetime

class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")

        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
        
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

########################################### Task 2 (Write a class from scratch)
# Write the class Point as outlined in the instructions
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**(0.5)
    
    def reflect(self,axis):
        if axis == "x":
            self.y =  -self.y
        elif axis == "y":
            self.x = -self.x
        else:
            print("Invalid")

pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())

