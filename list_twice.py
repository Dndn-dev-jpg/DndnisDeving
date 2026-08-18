# Write your solution here
my_list = []
while True : 
    meow = int(input("New item: "))
    if meow == 0 : 
        print("Bye!") 
        break
    my_list.append(meow)
    inorder = sorted(my_list)
    print(f"The list now: {my_list}")
    print(f"The list in order: {inorder}")