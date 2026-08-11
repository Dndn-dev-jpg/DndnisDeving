string = str(input("Please type in a string: "))
substr = str(input("Please type in a substring: "))
index = string.find(substr)
previous = index + len(substr)
if index == -1 :
    print("The substring does not occur twice in the string.")
else : 
    index = string.find(substr , previous)
    if index == -1 :
        print("The substring does not occur twice in the string.")
    else : 
        print(f"The second occurrence of the substring is at index {index}.")