sentence = str(input("Please type in a sentence: "))
while True :
    print(sentence[0])
    index = sentence.find(" ")
    if index == -1  :
        break
    sentence = sentence[index + 1 : ]