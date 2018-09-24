from math import sqrt
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

if a<=0 and b<=0 and c<=0:
    print("Invalid Input")
else:
    if a<(b+c) and b<(c+a) and c<(a+b):
        print("Triangle IS POSSSIBLE ")
        if a == b and a == c and b == c:
            print("Equilateral Triangle")
        elif c == sqrt(a ** 2 + b ** 2) or b == sqrt(a ** 2 + c ** 2) or a == sqrt(b ** 2 + c ** 2):
            print("Right Angled Triangle")
        elif a==b or b==c or c==a:
            print("Isolous Triangle")
        else:
            print("Scalene Triangle")

    else:
        print("Triangle Not possible")




