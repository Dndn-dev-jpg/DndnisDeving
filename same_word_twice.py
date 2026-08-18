# Write your solution here
kow = []
while True : 
    meow = str(input("Word: "))
    if meow in kow : 
        print(f"You typed in {len(kow)} different words")
        break
    kow.append(meow)
