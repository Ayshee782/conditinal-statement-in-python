"""takes a temperature input in Celsius 
and prints "Cold" if it's below 10°C, 
"Warm" if it's between 10°C and 30°C, 
and "Hot" if it's above 30°C."""

a=float(input("enter temperature= "))
if((a<=10)or(a==10)):
    print("cold")
elif((a>=10)and(a<=30)):
    print("warm")
else:
    print("hot")