string = str(input("Please type in a string: ")) 
meow = len(string) + 1
while meow >= 0 : 
    print(string[meow : (len(string)+1)])
    meow -= 1