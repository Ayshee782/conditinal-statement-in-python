"100-90=A , 90-80=B, 80-70=C, 70=D,"
a=int(input("enter marks="))
print(a)
if(100>=a>=90):
    print("A")
elif(90>=a>=80):
    print("B")
elif(80>=a>=70):
    print("C")
elif(70>=a>=60):
    print("D")
else:
    print("fail")