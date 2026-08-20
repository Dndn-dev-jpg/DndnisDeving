# Write your solution here
def palindromes(string) : 
    stow = string[::-1]
    return string == stow

name = ""
while name != True: 
    meow = input("Please type in a palindrome: ")
    name = palindromes(meow)
    if name == False : 
        print("that wasn't a palindrome")
    else : 
        print(f"{meow} is a palindrome!")
