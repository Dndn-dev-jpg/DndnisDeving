# Write your solution here
def first_word(string) : 
    index = string.find(" ")
    return string[0 : index] 
def second_word(string) : 
    index = string.find(" ")
    index += 1
    meow = string.find(" " , index)
    if meow == -1 : 
        return string[index : ]
    return string[index : meow ]
def last_word(string):
    index = -1 
    while string[index] != " " :
        index -= 1 
    return string[(index + 1): ]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))