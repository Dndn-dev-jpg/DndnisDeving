word = str(input("Please type in a word: ")) 
character = str(input("Please type in a character: ")) 
index = word.find(character)
if index <= (len(word) - 3) and index != -1 :  
    print(word[index : (index + 3)])
