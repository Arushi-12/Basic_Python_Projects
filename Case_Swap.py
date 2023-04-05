#This program swaps the case of the letters in string entered as input
str1=input("enter a string")
for i in range(0,len(str1)):
    print(str1[i].swapcase(),end='')
