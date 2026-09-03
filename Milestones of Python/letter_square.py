# Write your solution here
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
layers = int(input("Layers: "))
sides = (layers)*2 - 1
for rows in range(sides):
    for column in range(sides):
        top = [rows , abs(rows - (sides - 1)), column ,abs(column - (sides - 1))]
        letters = alphabet[(layers - 1) - min(top)]
        print(letters , end="")   
    print()



