# Object-Oriented Programming

### 1. Procedural Programming vs Object-Oriented Programming :
Procedural Programming
    1. Code as sequence of steps
    2. Great for data analysis and scripts

Object-Oriented Programming 
    1. Code is interactions of objects
    2. Great for building frameworks and tools
    3. Maintanable and reusable code

Object = state + behaviour
States contains attributes (variables)
Behavioir contains method (function)

### 2. Encapsulation
Bundling data with code operating on it.

### 3. Class
Blueprint for objects outlining possible states and behaviours.

### 4. Objects in Python
- Everything in python is an object
- Every object has class
- use type to find class
- Methods are functions, so anything you can do with a function, you can also do with a method.

### 5. Key Terms
1. Method (a.k.a Function)
    ```
    import numpy as np
    a = np.array([1,2,3,4])
    # reshape is an example of method
    a.reshape(2,2)
    ```
2. atributes (a.k.a parameters)
    ```
    import numpy as np
    a = np.array([1,2,3,4])
    # shape is an example of atributes
    a.shape
    ```

3. arguments 
4. parameters
5. Class constructor
    ```
    ## __init__() is an class constructor (allow create multiple atributes in a single method)
    class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
    ```
6. Class
    ```
    class Employee:
        pass
    ```
7. Function
    ```
    def set_count(self,n):
        self.count = n
    ```

8. Instance Atributes
    ```
    ## __init__(self) with only self parameters is an instance atributes
    # Create a Player class
    class Player:
        MAX_POSITION = 10
        
        def __init__(self):
            self.position = 0
    ```
9. Encapsulation
10. Polymorphism
11. Inheritance (warisan)
    Inheritance is a powerful tool of object-oriented languages that allows you to customize functionality of existing classes without having to re-implement methods from scratch.
    ```
    # Parent      
    class BankAccount:
        def __init__(self,balance):
            self.balance = balance
        
        def withdraw(self,amount):
            self.balance -= amount
    
    # Child (Inheritance)
    # Empty class inherited from BankAccount
    class SavingAccount(BankAccount):
        pass     
    ```
12. Object
    ```
    # create object from Employee Class
    emp = Employee()
    ```
13. Class Instance
    ```
    ## 
    class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
    ```
14. Decorator
    ```
    # @classmethod is characteristic of decorator
    class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod # decorator
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
    ```

## Source
1. https://drive.google.com/drive/folders/1YoZTG6ktqL1q5gEYjBOsiu-iAoJJIYKE


