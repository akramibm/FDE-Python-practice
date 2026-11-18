#Data Types
#int,float,complex,bool,str,list,tuple,range,dic,set

# Integer data type is used to represent whole numbers without any decimal point. It can be positive, negative, or zero. Integers are commonly used for counting, indexing, and performing arithmetic operations.age = 25  # Integer
age = 25  # Integer
count = 10  # Integer
temperature = -5  # Integer
print(age)  # Output: 25
 

print(type(age).__name__)  
print(count)  # Output: 10   #output: <class 'int'>
print(type(count).__name__)  
print(temperature) #output: <class 'int'>
print(type(temperature).__name__)  #output: <class 'int'>



#Float data type is used to represent numbers with decimal points. It can also represent scientific notation. Floats are commonly used for measurements, calculations involving fractions, and representing continuous values.
price = 19.99  # Float
height = 5.8  # Float
print(price)  # Output: 19.99
print(type(price).__name__)   #output: <class 'float'>
print(height)  # Output: 5.8
print(type(height).__name__)  #output: <class 'float'>

#complex data type is used to represent complex numbers, which consist of a real part and an imaginary part. Complex numbers are commonly used in mathematics, physics, and engineering applications.
z1 = 2 + 3j  # Complex number
print(z1)
print(type(z1).__name__)  #output: <class 'complex'>

#bool data type is used to represent boolean values, which can be either True or False. Booleans are commonly used in conditional statements and logical operations.
is_active = True  # Boolean
is_complete = False  # Boolean
print(is_active)  # Output: True
print(type(is_active).__name__)  #output: <class 'bool'>
print(is_complete)  # Output: False
print(type(is_complete).__name__)  #output: <class 'bool'>


#str data type is used to represent strings, which are sequences of characters. Strings are commonly used for text manipulation and storage.
name = "AKram"  # String
message = "Hello, World!"  # String
print(name)  # Output: "John"
print(type(name).__name__)  #output: <class 'str'>
print(message)  # Output: "Hello, World!"
print(type(message).__name__)  #output: <class 'str'>

#list data type is used to represent ordered collections of items and allow duplicates. Lists can contain elements of different data types and are mutable, meaning their contents can be modified after creation. Lists are commonly used for storing and manipulating collections of data.
list1 = ["apple", "FDE", "-1"]  # List
print(list1)  # Output: ["apple", "FDE", "-1"]   
print(type(list).__name__)  #output: <class 'list'>

#tuple data type is used to represent ordered collections of items, similar to lists, but tuples are immutable, meaning their contents cannot be modified after creation. Tuples can contain elements of different data types and are commonly used for grouping related data together.
coordinates = (10, 20, 60)  # Tuple
print(coordinates)  # Output: (10, 20, 60)
print(type(coordinates).__name__)  #output: <class 'tuple'>

#set data type is used to represent unordered collections of unique items. Sets do not allow duplicate elements and are commonly used for membership testing, removing duplicates from a collection, and performing mathematical set operations.
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
print(type(unique_numbers).__name__)  #output: <class 'set'>


#dict data type is used to represent key-value pairs, where each key is unique and maps to a corresponding value. Dictionaries are commonly used for storing and retrieving data based on keys.
person = {"name": "John", "age": 30, "city": "New York"}  # Dictionary
print(person)
print(type(person).__name__)  #output: <class 'dict'>


#None datatype if any value is missing 

res=None
print(type(res).__name__)
## range sequesnce of integer 
# Syntax: range(start, stop, step)
number = range(1, 10)  # Starts at 1, stops before 10

print(number)                 # Output: range(1, 10)
print(list(number))           # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(number).__name__)  # Output: range
print(type(number))           # Output: <class 'range'>

#Converison types process
#convert a value one data type to another data type

#float to int
a=10.5
b=5    
c=int(a+b)
print(c)  # Output: 15
print(type(c).__name__)  # Output: int   


# string to integer
age_int="25"
age_int=int(age_int)
print(age_int)  # Output: 25
print(type(age_int).__name__)  # Output: int

#string to list
string_value = "Hello, World!"
list_value = list(string_value)
print(list_value)  # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
print(type(list_value).__name__)  # Output: list

#string to tuple
string_value = "25"
tuple_value = tuple(string_value)   
print(tuple_value)  # Output: ('2', '5')
print(type(tuple_value).__name__)  # Output: tuple

#string to set
string_value = "Hello, World!"  
set_value = set(string_value)
print(set_value)  # Output: {'H', 'e', 'l', 'o', ',', ' ', 'W', 'r', 'd', '!'}
print(type(set_value).__name__)  # Output: set

# #string to float not possible ValueError: could not convert string to float: 'Hello, World!'
# string_value = "Hello, World!"
# float_value = float(string_value)   
# print(float_value)  # Output: 3.14
# print(type(float_value).__name__)  # Output: float

# string to dict not possible ValueError: dictionary update sequence element #0 has length 1; 2 is required
# string_value = "Hello, World!"
# dict_value = dict(string_value)
# print(dict_value)  # Output: {'H': None, 'e': None, 'l': None, 'o': None, ',': None, ' ': None, 'W': None, 'r': None, 'd': None, '!': None}
# print(type(dict_value).__name__)  # Output: dict   


##small example

price = float(input("Enter the price: "))  # Convert user input to float
quantity = 2
total_cost = price * quantity
print(f"Total cost: {total_cost}")  # Using f-string to format the output


#input and output functions
#used to accept the data from user through keyboard while program running

#example
name = input("Enter your name: ")  # default is string
print(f"Hello, {name}!")  # Using f-string to greet the user
print(type(name).__name__)  # Output: str

#example for int input 
age1 = int(input("Enter your age: "))  # Convert user input to int
print(f"You are {age1} years old.")  # Using f-string to display the age
print(type(age1).__name__)  # Output: int

#example for float input
height1 = float(input("Enter your height in meters: "))  # Convert user input to
print(f"Your height is {height1} meters.")  # Using f-string to display the height
print(type(height1).__name__)  # Output: float

# fstring
# it was introduced in python3.6

#fstring example
name = "chitti"
print(f"hello {name}")


name = "chitti"
age = 30
weight = 50

print ("My name is " + name + ", I am " + str(age) + "years old")
print ("my name is ", name, "I am", age, "years old")
veer=f"my name is {name} I am {age/2} years old"
print(veer)