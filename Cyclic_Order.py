#This program runs a string in cyclic order i.e. abc becomes bca and cab
str1=input("enter a string")
for i in range(0,len(str1)):
    print(str1[i:] + str1[:i])
