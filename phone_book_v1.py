# Write your solution here
dictionary = {}
while True : 
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3 : 
        print("quitting...")
        break
    if command == 2 : 
        name = str(input("name: "))
        number = input("number: ")
        dictionary[name] = number
        print("ok!")
    if command == 1 : 
        name = str(input("name: "))
        if name in dictionary : 
            print(dictionary[name])
        else :
            print("no number") 