# This program tells us the count of the alphabets , numbers and the spaces present in a string
str1=input("enter a string")
a=0
d=0
s=0
for i in range(0,len(str1)):
    if str1[i].isalpha():
        a+=1
    if str1[i].isdigit():
        d+=1
    if str1[i].isspace():
        s+=1
print("number of alphabets=",a)
print("number of digits=",d)
print("number of spaces=",s)
