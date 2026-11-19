# while loop
# while loop is used to repeat block of code as long as given conditon true
# while loop can use index (i) to access list of elements
# for loop is used to iterate over the sequence of elements (list, tuple, dictionery )

#example while infinte loop

# while True :
#     print("Hello")

#infinity loop print 1
# i=1
# while True:
#     print(i)

#infinity loop print sequence order 0,1,2
# i=0
# while True:
#     print(i)
#     i +=1

# i=1

# while i <= 10 :
#     print(i)
#     i+=1


i=0

while i <= 10 :
    print(i)
    i+=1


# example while with range

i=1
while i in range(1,6):
    password= input("Enter the Password: ")
    if password =="Saira@123":
        print("*****Access granted Allowed to login*****")
        break
    else:
        print("*****Access Denied not Allowed to login***")
        
    i = i + 1



#for loop example for AI Assistant

for i in range(1,4):
    question= input("Ask Question to AI: ")
    if question.lower() == "exit":
        print("Stop")
        break
    else:
        print("AI is responding")

#i can able to ask howmany questions? 3 questions

while True:
    question= input("Ask Question to AI: ")
    if question.lower() == "exit":
        print("Chatbot Stopped")
        break
    print("AI is responding")


#for loop range continue example

for i in range(1,6):
    if i==2:
        continue
    if i==4:
        break
    print(i)


for i in range(1,6):
    if i==3:
        continue
    print(i)


    



