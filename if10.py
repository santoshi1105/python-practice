a=float(input("Enter first number"))
b=float(input("Enter second number"))
c=float(input("Enter third number"))
if a>b and a>c:
    print("greatest number is",a)
    if b>c and b>a:
        print("greatest number is",b)
else :
            print("greatest number is",c)
