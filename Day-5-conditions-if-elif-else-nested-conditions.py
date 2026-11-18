#Indentation and Syntax
#Indentation means adding spaces begining line of the code.

#example of indentation
if True:
    print("This is indented")  # This line is indented with 4 spaces


c=10
b=20
if c < b:
    print("c is less than b")  # This line is indented with 4 spaces
    print(f"c = {c}, b = {b}")
else:
    print("c is not less than b")  # This line is indented with 4 spaces
    print(f"c = {c}, b = {b}")



c=30
b=20
if c < b:
    print("c is less than b")  # This line is indented with 4 spaces
    print(f"c = {c}, b = {b}")
else:
    print("c is not less than b")  # This line is indented with 4 spaces
    print(f"c = {c}, b = {b}")

c=1
a=10

if c == 15:
    print(c)  # This line is indented with 4 spaces
else:
    print("Not Found")  # This line is indented with 4 spaces
print (a)


#short-hand way 
a=6
if a>5: print("hello")

a=2
print(a)


# Python Conditions if, elif, else, Nested condition
# Rule-1: use colon (:) every if , else, elif
# Rule-2: Indentation mandatory
# Rule -3: elif, else cannot stand alone
# correct indetattiion exmaple

#example simple if

age=20
if age >= 18:
    print("Adult")
    print("You are eligible to vote.")


#simple if-else example
age=16
if age >= 18:
    print("Adult")
    print("You are eligible to vote.")
else:
    print("Minor")
    print("You are not eligible to vote.")

#pass value dynamically using input() 
#by default input function consider struing 

age = int(input("Enter your age: "))  # Convert user input to integer
if age >= 18:
    print("Adult")
    print("You are eligible to vote.")
else:
    print("Minor")
    print("You are not eligible to vote.")


## example lagin creds validations 

password = "secret123"

if password == "secret123":
    print("Access granted")
else:
    print("Access denied")



#example of if, elif, else
a= 10
if a > 15:
    print("a is greater than 15")
elif a > 5:
    print("a is greater than 5 but less than or equal to 15")
else:
    print("a is less than or equal to 5")



#example2 if elif

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("fail")


#Nested conditions
#conditon inside the condition

#example of nested conditions
marks = 75
if marks >= 60:
    print("You have passed.")
    if marks >= 90:
        print("Excellent performance!")
    elif marks >= 80:
        print("Good job!")
    else:
        print("Keep improving!")



