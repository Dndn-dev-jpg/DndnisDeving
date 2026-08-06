typed = 0
some = 0
negative = 0
postive = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True :
    numbers = int(input("Number: "))
    if numbers == 0 :
        break
    else :
        typed += 1
        some += numbers
        if numbers < 0 : 
            negative += 1
        else : 
            postive += 1
print(f"Numbers typed in {typed}") 
print(f"The sum of the numbers is {some}")
print (f"The mean of the numbers is {float(some / typed)}")
print(f"Positive numbers {postive}")
print(f"Negative numbers {negative}")