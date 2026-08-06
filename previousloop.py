sentence = ""
previous = ""
while True:
    word = input("Please type in a word: ")
    if word == "end" :
        break
    if previous == word :
        break
    if sentence == "":
        sentence = word
    else:
        sentence = sentence + " " + word
    previous = word
print(sentence)