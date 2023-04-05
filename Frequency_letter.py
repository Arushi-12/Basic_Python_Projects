#This program counts the frequecy i.e. the occurrence of a specific letter in the string
str1=input("enter a string")
n=input("enter a alphabet")
c=0
freq=0
for i in range(0,len(str1)):
    if str1[i]==n:
        c=c+1
print("count=",c)        
freq=c/len(str1)*100
print("frequency of alphabet=",freq)
