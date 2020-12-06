##################################### Core Principal of OOP ##################################
# 1. INHERITANCE
# 2. POLYMORPHISM
# 3. ENCAPSULATION

#################################### Task 1 (Class-level attributes)
# Create a Player class
class Player:
    MAX_POSITION = 10
    
    def __init__(self):
      self.position = 0

# Print Player.MAX_POSITION  
print(Player.MAX_POSITION)   

# Create a player p and print its MAX_POSITITON
p = Player()
print(p.MAX_POSITION)

class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position += steps
        else:
            self.position = Player.MAX_POSITION
           
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()

#################################### Task 2 (Changing class attributes)
### Sub Task 1
# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# ---MODIFY THIS LINE--- 
p1.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)

### Sub Task 2
# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# ---MODIFY THIS LINE--- (assigned 7 to it, without touching the class attribute.) 
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)


#################################### Task 3 (Changing class attributes)
##### Sub Task 1
class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)

##### Sub Task 2
# import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
      
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls,datetime):
        year, month, day = today.year, today.month, today.day 
        return cls(year,month,day)

# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)

####################################### Class Inheritance #######################################
# New Class Functionality = Old Class Functionality + extra
# Examples

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    
    def withdraw(self,amount):
        self.balance -= amount

# Empty class inherited from BankAccount
class SavingAccount(BankAccount):
    pass     

##################################### Task 1 
class Counter:
    def __init__(self, count):
       self.count = count

    def add_counts(self, n):
       self.count += n

class Indexer(Counter):
   pass


# #### True Statements
# - Inheritance represents is a-relationship
# - If ind is an Indexer object, then isinstance(ind,Counter) will return True
# - Running ind = Indexer() will cause an error
# - Class Indexer is inherited from Counter

# #### False Statements
# - Every Counter object is an Indexer object
# - Inheritance can be used to add some of the parts of one class to another class
# - If ind is an indexer object, then running ind.add_counts(5) will cause an error

########################################## Task 2 (Create a subclass)
###### Sub Task 1
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
  pass

# Define a Manager object
mng = Manager("Debbie Lashko",86500)

# Print mng's name
print(mng.name)

###### Sub Task 2
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
  def give_raise(self, amount):
    self.salary += amount      
        
# MODIFY Manager class and add a display method
class Manager(Employee):
  def display(self):
    print("Manager",self.name)

mng = Manager("Debbie Lashko", 86500)
print(mng.name)

# Call mng.display()
mng.display()

##################################### Customizing Functionality via Inheritance ###########################
# we can (1) Call Constructur (2) add new function 

### Parent Class
class BankAccount:
  def __init__(self, balance):
    self.balance = balance
  
  def withdraw(self, amount):
    self.balance -= amount


### Inherited Class
class SavingAccount(BankAccount):
  def __init__(self, balance, limit):
    BankAccount.__init__(self, content) # call constructor from parent class
    self.limit = limit
  
  def deposit(self, amount):
    self.balance -= amount 

  def withdraw(self, amount, fee=0):
    if fee <= self.limit:
      BankAccount.withdraw(self, amount - fee)
    else:
      BankAccount.withdraw(self, amount - self.limit)

###################################### Task 1 (Method inheritance) 
### Sub Task 1
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
  # Add a constructor 
    def __init__(self, name, salary=50000, project=None):

        # Call the parent's constructor   
        Employee.__init__(self, name, salary)

        # Assign project attribute
        self.project = project 

  
    def display(self):
        print("Manager ", self.name)
 
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

### Sub Task 2        
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount,bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self,new_amount)
        
    
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)


######################################### Task 2 (Inheritance of class attributes)
# Create a Racer class and set MAX_SPEED to 5
class Racer(Player):
    MAX_SPEED = 5
 
# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_SPEED = ", p.MAX_SPEED)
print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)

######################################## Task 1 (Customizing a DataFrame)
# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
  def to_csv(self, *args, **kwargs):
    # Copy self to a temporary DataFrame
    temp = self.copy()    
    
    # Create a new column filled with self.created at
    temp["created_at"] = self.created_at
    
    # Call pd.DataFrame.to_csv on temp with *args and **kwargs
    pd.DataFrame.to_csv(temp,*args,**kwargs)



    

