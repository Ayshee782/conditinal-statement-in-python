#Write a program to check if a number is divisible by both 3 and 5

a= int(input("enter num="))
print (a)
b= (a%3==0)
c= (a%5==0)
if (b or c):
    print("hmm")