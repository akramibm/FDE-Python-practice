# Python Data structures
# str ---> collection of chracters ------>Immutable
# list --> collection of elements ------>Mutable
# tuple -->collection of elememnst ------>Immutable
# set ---->collection of unique element -->Mutable
# dict --> Key-vale-pairs ---------->Mutable

# String
# String indexing
# String Slicing
# String methods
# String immutability

# 1.1.String Indexing
# indexing :we can call individual letter from word

# Positive index start from 0 (left) ---->
# Negative index start from -1 (right) <---

#  0   1    2    3     4    5 

#  P   Y    T    H     O     N

#  -6    -5   -4   -3    -2    -1

#example for Positive index

word="PYTHON"
print(word[0])
print(word[3])
print(word[5])

## negtive index
word = "PYTHON"
print(word[-6])
print(word[-4])


word = "PYTHON"
print("last character:", word[-6])

# String Slicing
# slicing means extracting a portion of srting
# start index where slicing begins, included
# stop index where slicing ends, excluded
# step number of positions to shift
# Positive Step : start should be less than end (left to right) incremental slicing
# negative Step : start shoulod be grated than stop (right to left) Decremental slicing
# Ex: [start :stop : step]


word="PYTHON"
print(word[3:5])

#start is 3
#stop is 4
#output HO

print(word[3:3])
#no output
print(word[2:5])
#output THO

#start is 3
#stop is 4
## python slicing not give any erro if stop range is out of the range and als start point larger than end point 

#omitting the start index
print(word[:3])
print(word[:4])
print(word[:10])

#omitting the stop index
print(word[3:])
print(word[1:])
print(word[:])

#Negative slicing process
print(word[-4:3])
#output T

print(word[-4:2])
#no output


print(word[-4:-5:1])


print(word[-4:-5:-1])

print(word[-4:-6:-1])
#output TY

word = "veerafdedghst"
print(word[1:8:2])