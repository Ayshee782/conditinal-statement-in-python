#takes three numbers as input and prints the largest number.

a=int(input("enter the number a = "))
b= int(input("enter the number b = "))
c=int(input("enter the number  c = "))
if(a>b>c):
    print ("the largest number is a ")
elif(b>a>c):
    print ("the largest number is b")
else:
    print ("the largest number is c ")