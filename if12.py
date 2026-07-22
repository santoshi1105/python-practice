a=float(input("Enter length of first side"))
b=float(input("Enter length of second side"))
c=float(input("Enter length of third side"))
if a==b and b==c:
    print("it is Equilateral triangle")
elif a!=b and b!=c:
    print("it is a scalene triangle")
elif a==b or b==c and c==a:
    print("it is a isosceles triangle")
        
