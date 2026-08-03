from math import sqrt
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))
delta = (b**2) - 4*a*c
if a == 0:
    print("This is not a quadratic equation.")
if delta < 0 :
    print ("there is no solutions")
if delta == 0 :
    roota = (-b)/(2*a)
    print(f"The roots are {roota}")
if delta > 0 :
    roota1 = (-b + sqrt(delta))/(2*a)
    roota2 = (-b - sqrt(delta))/(2*a)
    print(f"The roots are {roota1} and {roota2}")









