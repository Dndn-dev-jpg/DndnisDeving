# Write your solution here
integer = int(input("Please type in a positive integer: "))
positive = integer + 1 
for i in range(integer , 0 , -1) :
    if i == 0 : 
        continue
    print(-i)
for i in range(positive) :
    if i == 0 : 
        continue
    print(i) 

