#Literals : A literal values wrtitten directly

age =15 # integer literal
price = 19.99 # float literal
name = "John" # string literal
is_student = True # boolean literal
registration_number = None # None literal
numbers = [1, 2, 3, 4, 5] # list literal mutable
coordinates = (10, 20) # tuple literal immutable
unique_numbers = {1, 2, 3, 4, 5} # set literal
user = {"name": "Alice", "age": 25} # dictionary literal key-value pair

# constants : A constant is a variable whose value cannot be changed once it is assigned. In Python, there is no built-in support for constants, but by convention, we use uppercase letters to indicate that a variable should be treated as a constant.
#Constant : Unchangeable value
pI = 3.14159 # constant for pi
DB_HOST = "localhost" # constant for database host
DB_PORT = 3306 # constant for database port

# Operators : An operator is a symbol that performs an operation on one or more operands. Python supports various types of operators, including arithmetic, comparison, logical, assignment, and more.

#Operators means special symbols

#Airthematic opeartors +, -, /, //, %, **
#Assignment opeartors =, +=, -=, *=, /=
#Comparison ==, !=, >, <, >= , <=
#Logical and, or, not
#Bitwise Operators &, | ~ << >>
#membership operators in, not in, is, is not

#arithmetic operators
a = 10
b = 3
c = a + b          # Addition
print("Addition:", c)   

a=5
b=7      
c= a-b
print("Subtraction:", c)  # Subtraction result is integer

a = 10
b = 3
c = a * b          # Multiplication
print("Multiplication:", c) # Multiplication result is integer

x= 10
y=21
z= x / y          # Division
print("Division:", z) # Division result is float

x= 20
y=11 
z= x // y          # Floor Division
print("Floor Division:", z) # Floor Division performs rounding the result down towards negative infinity to the nearest integer.

x= -9
y=5 
print(x/y) 

x= -9
y=5 
print(x//y) # Floor Division performs rounding the result down towards negative infinity to the nearest integer.


x=10
y=7
z= x % y          # Modulus
print("Modulus:", z) # Modulus returns the remainder of the division.

x=10
y=20
z=x%y
print("Modulus:", z) # when the dividend is smaller than the divisor, the modulus is equal to the dividend.


x= 2
y= 3    

z= x ** y          # Exponentiation
print("Exponentiation:", z) # Exponentiation raises the first operand to the power of the second operand. In this case, 2 raised to the power of 3 is 8.


#Comparison Opeartors ==,!=,a>b, a<b, a>=b, a<=b

a= 10
b= 20
print("Is a equal to b?", a == b) # False

a= 10
b= 20
print("Is a not equal to b?", a != b) # True

a= 10
b= 20       
print("Is a greater than b?", a > b) # False

a=30
b=20
print("Is a less than b?", a < b) # False

a=40
b=40
print("Is a greater than or equal to b?", a >= b) # True

age= 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#Logical Opeartors and, or, not

# and operator 
 # remeber both condition must be true 

#True    True     True
#True    False    False
#False   True     False 
#False   False    False 

#example
a=10
b=20
if a > 5 and b < 30:
    print("Both conditions are true.")


a=5
b=20
print(a > 5 and b < 30)
    
# or operator 
 # remeber one condition must be true 

#True    True     True
#True    False    True
#False   True     True 
#False   False    False 


# exmaple 
a= 3
b= 20
print ( a >5 or b > 15) #one condition true enough 

# exmaple 
a= 3
b= 20
print ( a >5 or b < 15) #one condition true enough 


#The not opeartor reverse the result
#not True ---> False 
#not False ---> True

#Memebrship Operators
#Memebrship operators use to check weather a value exist in a sequence or collection in , not in , is , is 
 #example

fruits = ["apple", "banana", "mango"]
print ("apple" in fruits)
print ("orange" not in fruits)
print ("orange"  in fruits)

