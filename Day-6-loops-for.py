# loops
# for, while , break , nested for loop, for loop if combination , for loop different types, operators
# indetation and syntax same process follw as if

#For loop we can use to iterate over the sequence of items,list,tuple,range,dict etc

a = "PYTHON"
for i in a:
    print(i)

# for loop with list
cloud = ["AWS", "AZURE", "GCP"]
for i in cloud:
    print(i)

#for loop with break
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i == 3:
        break
    print(i)


#for loop with dictionary
data = {"name": "John", "age": 30, "city": "New York"}
for key, value in data.items():
    print(key, ":", value)

#for loop with dictionary 
#for loop calling total items in dictionary
data = {"name": "John", "age": 30, "city": "New York"}
for i in data.items():
    print(i)

#for loop with dictionary
#for loop calling only keys in dictionary
data = {"name": "John", "age": 30, "city": "New York"}
for key in data.keys():
    print(key)

#for loop with dictionary
#for loop calling only values in dictionary
data = {"name": "John", "age": 30, "city": "New York"}
for value in data.values():
    print(value)


#for loop with break
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i == 3:
        print("number 3 found, breaking the loop.")
        break
    print(i)

#for loop with range
total = 1
dev = range(1, 6)  # range(start, stop) - generates numbers from start to stop-1
for i in dev:
    total += i  # add i to total
print("Total:", total)  # print the final total

# first iteration 
#i=1
#total = total+i
       # = 1+1
#total =2


#second iteration 
#i =2
# total = total+i
# total =2+2
#     =4

#third iteration
#i =3
# total = total+i
# total =4+3
# total = 7

#4th itertaion 
#i =4
#total = total+i
#total = 7+4
#total = 11

#5th iteration
#i = 5
#total = total+i
#        = 11+5=16
#total 16


total = 2
dev = range(1, 6)  # range(start, stop) - generates numbers from start to stop-1
for i in dev:  
    total += i  # add i to total    
print("Total:", total)  # print the final total


#for loop example for Even and odd numbers

X= [1,2,3,4,5,6,7,8,9,10]
for i in X:
    if i % 2 == 1:
        print("number is even:", i)
    else:
        print("Numer is odd:", i)


# x variable 
# = assignement operator
# [1,2,3,4,5,6,7] List
# for Keyword
# i variable 
# in memebrship 
# if condition keyword
# %  airthematic operator
# == comparison operator
# print() Build-it functions
# else condition keyword
# indentation 
# : delimiter 


#example to python to find positive and negative number

numbers= [12,-2,0,55,34,-100]
for i in numbers:
    if i > 0 :
        print(f"{i} number is positive")
    elif i < 0:
        print(f"{i} number is Negative")
    else:
        print(f"{i} number is Zero")


import random

for i in range(1,2):
    num = random.randint(1,200)

    if num % 2 ==0 :
        print(f"number found {num} , iteration {i}")
        break
        print(f"try again {num} , iteration {i}")

    else:
        print(f"no odd numbers found in 4 attempts")


import random
for i in range(1,6):
    num = random.randint(1,200)
    if num % 2 == 0 :
            print(f"Even Number found {num} , | iteration {i}")    

    if num % 2 != 0 :
            print(f"odd Number found {num} , | iteration {i}") 

    if num > 50 :
         print(f" number is greater then 50 : {num}") 



