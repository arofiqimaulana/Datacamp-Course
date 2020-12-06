################################################ Designing for inheritance and polymorphism ####################################
# Polymorphism is a using unified interface to operate an objects of different classes
# Liskov Substitution Principle

############################################### Task 1 (using unified interface to operate an objects of different classes)
class Parent:
    def talk(self):
        print("Parent talking!")     

class Child(Parent):
    def talk(self):
        print("Child talking!")          

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild talking!")
        Parent.talk(self)


p, c, tc = Parent(), Child(), TalkativeChild()

for obj in (p, c, tc):
    obj.talk()

### Talk
# Parent talking!
# Child talking!
# Talkative Child talking!
# Parent talking

################################################# Task 2 (Square and rectangle)
# https://en.wikipedia.org/wiki/Circle%E2%80%93ellipse_problem

########## Sub Task 1
# Define a Rectangle class
class Rectangle:
    def __init__(self, h, w):
      self.h, self.w = h, w

# Define a Square class
class Square(Rectangle):
    def __init__(self, w):
      self.h, self.w = w, w 

########## Sub Task 3
class Rectangle:
    def __init__(self, w,h):
      self.w, self.h = w,h

# Define set_h to set h      
    def set_h(self, h):
      self.h = h
      
# Define set_w to set w          
    def set_w(self, w):
      self.w = w
      
      
class Square(Rectangle):
    def __init__(self, w):
      self.w, self.h = w, w 

# Define set_h to set w and h
    def set_h(self, h):
      self.h = h
      self.w = h

# Define set_w to set w and h      
    def set_w(self,w):
      self.h = w
      self.w = w
      
# Each of the setter methods of Square change both h and w attributes, while setter methods of Rectangle change only one 
# attribute at a time, so the Square objects cannot be substituted for Rectangle into programs that rely on one attribute staying constant.      

################################################# Managing data access : private #####################################################
# All data is public
# Restricting Access:
# 1. Naming conventions
# 2. Use @property
# 3. Overriding __getattr__() and __setattr__()

# obj._att_name, obj._method_name() -> As class user "dont touch this", As developer "use for implements details, helper function"
# obj.___att_name, obj.__method_name() -> Used to prevent name clashes in inherited class
# obj.___att_name__, obj.__method_name()__ -> Only use for built-in python

################################################ Task 1 (Exercise Attribute naming conventions)
# _name : A helper method that checks validity of an attribute's value but isn't considered a part of class's public interface
# __name : A `version` attribute that store the current version of the class and shouldn't be passed to child classes, who will have their own version 
# __name__ : A method that is run whenever the object is printed

############################################### Task 2 (Using internal attibutes)
# MODIFY to add class attributes for max number of days and months
# MODIFY to add class attributes for max number of days and months

class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTH = 12

    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
    
    # Add _is_valid() checking day and month values
    def _is_valid(self):
      if (self.day <= BetterDate._MAX_DAYS) & (self.month <= BetterDate._MAX_MONTH):
        return True
      else:
        return False

         
bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())

################################################ Properties ################################################
# You could think of properties as attributes with built-in access control. They are especially useful when there 
# is some additional code you'd like to execute when assigning values to attributes.

# Which of the following statements is NOT TRUE about properties?

# (1) Properties can be used to implement "read-only" attributes (TRUE)
# (2) Properties can prevent creation of new attributes via assignment (FALSE)
# (3) Properties can be accessed using the dot syntax just like regular attributes (TRUE) 
# (4) Properties allow for validation of values that are assigned to them (TRUE)

############################################### Create and set properties (Task 1)
############### Sub Task 1
# Create a Customer class
class Customer:
    def __init__(self,name,new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError('Invalid Balanced')
        self._balance = new_bal

Customer('test', 100)

############ Sub Task 2
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance

############ Sub Task 3
class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")

# Create a Customer        
cust = Customer("Belinda Lutz",2000)

# Assign 3000 to the balance property
cust.balance = 3000

# Print the balance property
print(cust.balance)

############################################### Read-only properties (Task 2)
import pandas as pd
from datetime import datetime

# MODIFY the class to turn created_at into a read-only property
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()
    
    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)   
    
    @property  
    def created_at(self):
        return self._created_at

ldf = LoggedDF({"col1": [1,2], "col2":[3,4]})

# Put into try-except block to catch AtributeError and print a message
try:
    ldf.created_at = '2035-07-13'
except AttributeError:
    print("Could not set attribute")
    











