word = str(input("Word: "))
character = str(input("Please type in a character: "))
previous = 0
while True :
    index = word.find(character , previous) 
    if index == -1 or index > (len(word) - 3) : 
        break
    else :
        print(word[index : (index + 3)])
        previous = index + 1