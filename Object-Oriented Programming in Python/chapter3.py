####################################################### Overloading equality (Task 1)
# fungsinya adalah memberitahu apakah dua objek sama atau tidak

class BankAccount:
   # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number
      
    def withdraw(self, amount):
        self.balance -= amount 
    
    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return self.number == other.number   

# Create accounts and compare them       
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)


###################################################### Checking class equality (Task 2)

class Phone:
  def __init__(self, number):
     self.number = number

  def __eq__(self, other):
    return self.number == \
          other.number

pn = Phone(873555333)

class BankAccount:
  def __init__(self, number):
     self.number = number

  def __eq__(self, other):
    return self.number == \
           other.number

acct = BankAccount(873555333)

## task
class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance
      
    def withdraw(self, amount):
        self.balance -= amount 

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))    

acct = BankAccount(873555333)      
pn = Phone(873555333)
print(acct == pn)

######################################################### Comparison and inheritance (Task 3)
class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return True

class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return True

p  = Parent()
q = Child()

p == q # Child's __eq__() called

######################################################## String formatting review (Task 4)

my_num = 5
my_str = "Hello"

f = ...
print(f)

# option a
f = "my_num is {0}, and my_str is {1}.".format(my_num, my_str)

# option b (The Right Answer)
f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str)

# option c
f = "my_num is {n}, and my_str is '{s}'.".format(n=my_num, s=my_str)

# option d
f = "my_num is {my_num}, and my_str is '{my_str}'.".format()

####################################################### String representation of objects (Task 5)
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      
    # Add the __str__() method
    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)


class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s
    
     # Add the __repr__method  
    def __repr__(self):
        s = "Employee(\"{name}\", {salary})".format(name=self.name, salary=self.salary)      
        return s   

emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))

####################################################### Exception ###################################################
####################################################### Task 1 (Catching exceptions) 
# MODIFY the function to catch exceptions
def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError:
        return print("Cannot divide by Zero!") 
    except IndexError:
        return print("Index out of range!")
 
a = [5,6,0,7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))

#################################################### Task 2 (Custom exceptions)
################### Sub Task 1
# Define SalaryError inherited from ValueError
class SalaryError(ValueError):
    pass

# Define BonusError inherited from SalaryError
class BonusError(SalaryError):
    pass

class Employee:
  MIN_SALARY = 30000
  MAX_RAISE = 5000

  def __init__(self, name, salary = 30000):
    self.name = name
    
    # If salary is too low
    if self.salary < MIN_SALARY:
      # Raise a SalaryError exception
      return print("Salary is too low!")
      
    self.salary = salary

)
################### Sub Task 2
      
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Rewrite using exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
       print("The bonus amount is too high!")  
        
    elif self.salary + amount <  Employee.MIN_SALARY:
       print("The salary after bonus is too low!")
      
    else:  
      self.salary += amount

################### Sub Task 3

class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Rewrite using exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
       raise BonusError()
        
    elif self.salary + amount <  Employee.MIN_SALARY:
       raise SalaryError()
      
    else:  
      self.salary += amount


####################################################### Task 2 (Handling exception hierarchies)
########### Sub Task 1
emp = Employee("Katze Rik", salary=50000)
try:
  emp.give_bonus(7000)
except SalaryError:
  print("SalaryError caught!")

try:
  emp.give_bonus(7000)
except BonusError:
  print("BonusError caught!")

try:
  emp.give_bonus(-100000)
except SalaryError:
  print("SalaryError caught again!")

try:
  emp.give_bonus(-100000)
except BonusError:
  print("BonusError caught again!")  

# conclution = except block for a parent exception will catch child exceptions

########### Sub Task 2
emp = Employee("Katze Rik",\
                    50000)
try:
  emp.give_bonus(7000)
except SalaryError:
  print("SalaryError caught")
except BonusError:
  print("BonusError caught")


emp = Employee("Katze Rik",\
                    50000)
try:
  emp.give_bonus(7000)
except BonusError:
  print("BonusError caught")
except SalaryError:
  print("SalaryError caught")
      
# conclution : 
# It's better to include an except block for a child exception before the block for a parent exception, 
# otherwise the child exceptions will be always be caught in the parent block, and the except block for the child will never be executed.

####################################################### Task 3 (Handling exception hierarchies)