lower=int(input("Enter the min range:"))
upper=int(input("Enter the max range:"))
for i in range (lower,upper+1):
    if(i%7==0 and i%5==0):
        print(i)