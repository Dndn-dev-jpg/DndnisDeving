print("Person 1:")
prsn1 = input("Name: ")
age1 = int(input("age: "))
print("Person 2:")
prsn2 = input("Name: ")
age2= int(input("age: "))
if age1 > age2 :
    print(f"The elder is {prsn1}")
elif age1 < age2 : 
    print(f"The elder is {prsn2}")
else : 
    print(f"{prsn1} and {prsn2} are the same age")