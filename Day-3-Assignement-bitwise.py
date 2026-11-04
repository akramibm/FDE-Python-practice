#Assignment Operators
#Assignment operators are used to assign values to variables. The most common assignment operator is the equal sign (=), which assigns the value on the right to the variable on the left.


x=10  # Assigns the value 10 to the variable x
x +=5  # Adds 5 to the current value of x and assigns the result back to x
print(x)


x=10
x -= 5
print(x)  # Subtracts 30 from the current value of x and assigns the result back to x


x=45
x *= 2
print(x)  # Multiplies the current value of x by 2 and assigns the result back to x

x=10
x /= 2  
print(x)  # Divides the current value of x by 2 and assigns the result back to x


#increment and decrement operators
#Python does not have built-in increment (++) or decrement (--) operators like some other programming
#languages. Instead, you can achieve the same effect using the += and -= operators.

x= 5
x += 1  # Increment x by 1  
print(x)  # Output: 6

x= 9
x -= 4  # Decrement x by 4  
print(x)  # Output: 5

x= 10
x *= 3  # Multiply x by 3
print(x)  # Output: 30

x= 20
x /= 4  # Divide x by 4
print(x)  # Output: 5.0

x= 15
x %= 4  # Get the remainder of x divided by 4
print(x)  # Output: 3

x = 2
x **= 3  # Raise x to the power of 3
print(x)  # Output: 8

#Left shift 
#left shift operator (<<) shifts the bits of a number to the left by a specified number of positions. Each left shift effectively multiplies the number by 2 for each position shifted.
left_shift = 5 << 1  # Left shift the binary representation of 5 by 1 position
print("Left Shift:", left_shift)  # Output: 10 (binary 101 becomes 1010)


#Left shift
x=15
x<<=1
print(x)

# before binary 1111
# after binary0  1111  
#left shift (<<) : move bits left and add bit postion on right 0

x =19  #10011
x<<=2  #10011000
print (x)

# try 
x=21
x<<=3 
print (x)

#Right shift operators (>>) shift the bits of a number to the right by a specified number of positions. Each right shift effectively divides the number by 2 for each position shifted, discarding any remainder.
right_shift = 10 >> 1  # Right shift the binary representation of 10 by 1 position
print("Right Shift:", right_shift)  # Output: 5 (binary 1010 becomes 101)


x= 15
x>>=1
print (x)

# >>1 
#before x=15 1111
#after   0111   

# right shift 
x= 15
x>>=4
print (x)

# >>1 
#before x=15 1111
#after   0011 

#right shift >> mobe bits right and discard the right most bits 

# #Left shift 
# 15        1111
# 15 << 1   11110
# 15 << 2   111100
# 15 << 3   1111000
# ## Right shift
# 15        1111
# 15 >>1    0111
# 15 >>2    0011
# 15 >>3    0001

#bitwise operators
#Bitwise operators are used to perform bit-level operations on binary representations of integers. These operators work directly on the individual bits of the numbers, allowing you to manipulate and analyze data at the binary level. The common bitwise operators in Python include AND (&), OR (|), NOT (~), XOR (^), left shift (<<), and right shift (>>).


# Bitwise Operators
# Bitwise AND
# Bitwise OR
# Bitwise XOR
# Bitwise Not

a= 5  # Binary: 0101
b= 3  # Binary: 0011    
print("Bitwise AND:", a & b)  # Output: 1 (Binary: 0001)

a = 5  # Binary: 0101
b = 3  # Binary: 0011   
print("Bitwise OR:", a | b)  # Output: 7 (Binary: 0111)

a = 5  # Binary: 0101
b = 3  # Binary: 0011   
print("Bitwise XOR:", a ^ b)  # Output: 6 (Binary: 0110)

a = 5  # Binary: 0101
b = 3  # Binary: 0011   
print("Bitwise NOT:", ~a)  # Output: -6 (Binary: 11111010)

