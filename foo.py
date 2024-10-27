#################################################################################
#           PYTHON IN LESS THAN 300 LINES | MADE WITH ❤ BY REDACTADO           #
#################################################################################

# This is a comment, it is ignored by the interpreter. You can use it to write notes to yourself or others.

# VARIABLES

# Define a variable
foo = 0 # We are defining a INT type variable, for that we say that foo equals ( = ) to 0

# We can add to this variable by using the += operator, this works also for strings by adding them together.
foo += 1 # foo now equals 1

# We can also subtract from this variable by using the -= operator
foo -= 1 # foo now equals 0, because before it was 1

# Now we have the variable foo, but as array. We can add to this array by using the append() method
foo = [] # foo is now an array

foo.append(1) # foo now equals [1]
foo[0] += 1 # foo now equals [2], because we are selecting the first element of the array and adding 1 to it.

# Arrays can contain inside them other arrays, this is called a multidimensional array. This is useful for storing data in a grid, altrough you won't need it right now.
foo2 = [[1, 2], [3, 4]] # foo2 is now a multidimensional array

print(foo2[0][0]) # This will print 1, because we are selecting the first element of the first array inside foo2 and printing it with print()



# FUNCTIONS

# We can detect something is a function because it has a name, and it is followed by parentheses. Functions can take arguments, which are the values that the function will use to do something.
# A clear example is the print function, which takes a string as an argument and prints it to the console.

# Now we are going to make our own function, it will take a number as an argument and return it multiplied by 2.
def multiply_by_two(number): # We are defining a function called multiply_by_two, which takes a number as an argument
    return number * 2 # We are returning the number multiplied by 2  with the return method, that gives a response to the function call, this is the same as if we were to write number * 2


# CONDITIONALS AND LOOPS

# We can use conditionals to make decisions in our code, for example, we can use an if statement to check if a number is greater than 5.
foo = 6 # Now foo equals to 6

if foo > 5: # If foo is greater than 5
    print("foo is greater than 5") # Print this string

# We can also use an else statement to do something if the condition is not met
if foo > 5: # If foo is greater than 5
    print("foo is greater than 5") # Print this string
else:
    print("foo is not greater than 5")

# We can also use an elif statement to check for multiple conditions, same as the else statement, but with a condition
# Now we are going to see all conditions we can add to an if statement

# Starting from basic signs: >, <, >=, <=, ==, != (greater than, less than, greater or equal, less or equal, equal, not equal)
# We can also use the and, or, and not operators to combine conditions
# Here is an example.

foo = [1, 2, 3, 4, 5] # Now foo is an array with numbers from 1 to 5

if (3 in foo and len(foo) == 5) or foo[4] == 5: # If 3 is in the first element of foo and the length of foo is 5, or the last element of foo is 5
    print("The conditions are met") # Print this string

# We can also use loops to repeat code, for example, we can use a for loop to print all the elements of an array
foo = [1, 2, 3, 4, 5] # Now foo is an array with numbers from 1 to 5

for number in foo: # For each number in foo
    print(number) # Print the number

# The for structure requires 2 things: a variable to store the current element of the array, and the array itself.
# The first argument (the one we put exacly after the for keyword) is the variable that will store the current element of the array, it can be whatever, it won't affect the resut.
# The second argument is the array itself, it can be a variable, or a list of elements, or a range of numbers. Must be a real variable or a list of elements, not a string or a number.

# for loops can also be used to get all letters of a string
foo = "Hello, World!" # Now foo is a string
for letter in foo: # For each letter in foo
    print(letter) # Print the letter

# We can also use a while loop to repeat code until a condition is met
foo = 0 # Now foo equals 0
while foo < 5: # While foo is less than 5
    print(foo) # Print foo
    foo += 1 # Add 1 to foo

# The while structure requires a condition, which is the same as the one we use in an if statement, and the code that will be repeated until the condition is met.
# The condition can be anything, as long as it returns a boolean value (True or False), if it returns a number, it will be treated as False if it is 0, and True if it is any other number.
# The code that will be repeated can be anything, it can be a single line of code, or a block of code, which is a group of lines of code that are indented, like the ones we use in functions or conditionals.

# We can also use the break and continue statements to control the flow of a loop
foo = 0 # Now foo equals 0
while True: # While True (this is an infinite loop)
    if foo == 5: # If foo is 5
        break # Stop the loop
    print(foo) # Print foo
    foo += 1 # Add 1 to foo

# Try to  guess what this code will do before running it, then run it and see if you were right.

# The break statement stops the loop, and the continue statement skips the rest of the code in the loop and goes to the next iteration.
foo = 0 # Now foo equals 0
while foo < 5: # While foo is less than 5
    if foo == 3: # If foo is 3
        foo += 1 # Add 1 to foo
        continue # Skip the rest of the code and go to the next iteration
    print(foo) # Print foo
    foo += 1 # Add 1 to foo

# Try to  guess what this code will do before running it, then run it and see if you were right.


# CLASSES

# We can use classes to define objects, which are a group of variables and functions that are related to each other.
# For example, we can use a class to define a person, which has a name and an age.

class Person: # We are defining a class called Person
    def __init__(self, name, age): # We are defining a function called __init__, which is the constructor of the class, it is called when we create a new object of the class
        self.name = name # We are defining a variable called name, which is a string, and we are setting it to the value of the name argument
        self.age = age # We are defining a variable called age, which is an int, and we are setting it to the value of the age argument

    def greet(self): # We are defining a function called greet, which takes no arguments
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old") # We are printing a string with the name and age of the person

# Now we are going to create a new object of the Person class and call the greet function
person = Person("John", 30) # We are creating a new object of the Person class, with the name John and the age 30
person.greet() # We are calling the greet function of the person object

# We can also use classes to define more complex objects, for example, we can use a class to define a car, which has a brand, a model, and a color.

class Car: # We are defining a class called Car
    def __init__(self, brand, model, color): # We are defining a function called __init__, which is the constructor of the class, it is called when we create a new object of the class
        self.brand = brand # We are defining a variable called brand, which is a string, and we are setting it to the value of the brand argument
        self.model = model # We are defining a variable called model, which is a string, and we are setting it to the value of the model argument
        self.color = color # We are defining a variable called color, which is a string, and we are setting it to the value of the color argument

    def drive(self): # We are defining a function called drive, which takes no arguments
        print("The " + self.color + " " + self.brand + " " + self.model + " is driving") # We are printing a string with the brand, model, and color of the car

# Now we are going to create a new object of the Car class and call the drive function
car = Car("Toyota", "Corolla", "blue") # We are creating a new object of the Car class, with the brand Toyota, the model Corolla, and the color blue
car.drive() # We are calling the drive function of the car object

# When coding a big application, we might need an injector to inject dependencies into our classes, this is useful for testing and for making our code more modular.
# Altrough there are libraries to do this, like decoutilities (python) or guice (java), we can make our own injector, here is an example of how to do it.

class Injector: # We are defining a class called Injector
    def __init__(self): # We are defining a function called __init__, which is the constructor of the class, it is called when we create a new object of the class
        self.dependencies = {} # We are defining a variable called dependencies, which is a dictionary, and we are setting it to an empty dictionary

    def bind(self, key, value): # We are defining a function called bind, which takes a key and a value as arguments
        self.dependencies[key] = value # We are setting the value of the key in the dependencies dictionary to the value argument

    def get(self, key): # We are defining a function called get, which takes a key as an argument
        return self.dependencies[key] # We are returning the value of the key in the dependencies dictionary


# DECORATORS

# Decorators are useful for adding functionality to a function or a class without modifying its code, for example, we can use a decorator to log the arguments and return value of a function.

# Here is an example of a decorator that logs the arguments and return value of a function

def log(func): # We are defining a function called log, which takes a function as an argument
    def wrapper(*args, **kwargs): # We are defining a function called wrapper, which takes any number of arguments and keyword arguments
        print("Calling " + func.__name__ + " with arguments " + str(args) + " and keyword arguments " + str(kwargs)) # We are printing a string with the name of the function, the arguments, and the keyword arguments
        result = func(*args, **kwargs) # We are calling the function with the arguments and keyword arguments and storing the result in a variable
        print("Returning " + str(result)) # We are printing a string with the return value of the function
        return result # We are returning the result of the function
    return wrapper # We are returning the wrapper function

# Now we are going to use the log decorator to log the arguments and return value of the multiply_by_two function

@log # We are using the log decorator to log the arguments and return value of the multiply_by_two function
def divide_by_two(number):
    return number / 2

print(divide_by_two(10)) # This will print "Calling divide_by_two with arguments (10,) and keyword arguments {}" and "Returning 5.0"

# We can also use decorators to add functionality to a class, for example, we can use a decorator to log the arguments and return value of a method.
    


# MODULES

# We can use modules to organize our code into separate files, for example, we can use a module to define a person, which has a name and an age.

# Here is an example of a module that defines a person

# Path: person.py

class Person: # We are defining a class called Person
    def __init__(self, name, age): # We are defining a function called __init__, which is the constructor of the class, it is called when we create a new object of the class
        self.name = name # We are defining a variable called name, which is a string, and we are setting it to the value of the name argument
        self.age = age # We are defining a variable called age, which is an int, and we are setting it to the value of the age argument

    def greet(self): # We are defining a function called greet, which takes no arguments
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old") # We are printing a string with the name and age of the person

# Now we are going to use the person module to create a new object of the Person class and call the greet function

# Path: foo.py
from person import Person # We are importing the Person class from the person module

person = Person("John", 30) # We are creating a new object of the Person class, with the name John and the age 30
person.greet() # We are calling the greet function of the person object


# PACKAGES

# We can use packages to organize our modules into directories, for example, we can use a package to define a person, which has a name and an age.

# Here is an example of a package that defines a person

# Path: my_package/person.py

class Person: # We are defining a class called Person
    def __init__(self, name, age): # We are defining a function called __init__, which is the constructor of the class, it is called when we create a new object of the class
        self.name = name # We are defining a variable called name, which is a string, and we are setting it to the value of the name argument
        self.age = age # We are defining a variable called age, which is an int, and we are setting it to the value of the age argument

    def greet(self): # We are defining a function called greet, which takes no arguments
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old") # We are printing a string with the name and age of the person

# Now we are going to use the person module to create a new object of the Person class and call the greet function

# Path: foo.py
from my_package.person import Person # We are importing the Person class from the person module in the my_package package

person = Person("John", 30) # We are creating a new object of the Person class, with the name John and the age 30
person.greet() # We are calling the greet function of the person object

# We can also use the __init__.py file to define what modules are exported by the package, for example, we can use the __init__.py file to export the Person class.
# And also the __main__.py file to define the main function of the package, this is useful for running the package as a script.
# Sometimes we also might see a setup.py file, this is used to install the package, and it is used by the pip package manager.


# EXCEPTIONS (ERROR HANDLING)

# We can use exceptions to handle errors in our code, for example, we can use a try-except block to catch an exception and handle it gracefully.

# Here is an example of a try-except block that catches a ZeroDivisionError and prints an error message

try: # We are using a try block to try to do something
    result = 10 / 0 # We are trying to divide 10 by 0
except ZeroDivisionError:
    print("Error: division by zero")

# Creating own exceptions
# We can also create our own exceptions by defining a new class that inherits from the Exception class.

# Here is an example of a custom exception that is raised when a number is less than 0

class NegativeNumberError(Exception): # We are defining a class called NegativeNumberError that inherits from the Exception class
    pass # We are not adding any new functionality to the class

# Now we are going to raise the custom exception when a number is less than 0


number = -1 # Now number equals -1

if number < 0: # If number is less than 0
    raise NegativeNumberError("Number cannot be less than 0") # Raise the custom exception with an error message



# For the moment this is all you need to know about python, you can learn more about the language by reading the official documentation, or by reading books or watching tutorials.
# You can also learn by doing, by writing code and experimenting with it, this is the best way to learn programming.

# EXERCISES
# 🟢 - Easy
# 🔵 - Medium
# 🔴 - Hard

#🟢 1. Write a function that takes a number as an argument and returns the square of the number.

#🔵 2. Complete the following code to print all the even numbers from 1 to 10.

# for number in range(1,    ): # For each number from 1 to 10
#     if number % 2 == 0: # If the number is even
#         print(           ) # Print the number

#🟢 3. Write a function that takes a list of numbers as an argument and returns the sum of the numbers. The function must be 4 lines maximum.

#🔵 4. Using pip (python package manager), install the requests library and use it to make a GET request to the following URL: https://jsonplaceholder.typicode.com/posts/1

#🔵 5. Write a class called Circle that has a radius and a method called area that returns the area of the circle.

#🔴 6. Using pip (python package manager), install pygame, and make a Ping-Pong game using the library and the previously explained modular structure with injectors.

#🔵 7. Write a decorator that logs the time it takes to run a function.



# Good luck! 🚀
# Python in less than 300 lines made by Redactado
# Contact: contact@redactado.es | Website: https://redactado.es | Github: @Reddishye
# Finally, line 300, the end of the file.
