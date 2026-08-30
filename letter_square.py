# Write your solution here
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
layers = int(input("Layers: "))
sides = (layers)*2 - 1
for rows in range(sides):
    for column in range(sides):
        top = rows
        bottom = abs(top - (sides - 1))
        left = column
        right = abs(column - (sides - 1))
        variable = min(top , bottom , left , right)
        letters = alphabet[(layers - 1) - variable]
        print(letters , end="")   
    print()



