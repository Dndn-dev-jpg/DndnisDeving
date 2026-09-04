# write your solution here
meow = input("Write text: ")
index = 0
words = []
with open("wordlist.txt") as new_file :
    meow = meow.split()
    for line in new_file : 
        line = line.replace("\n" , "")
        words.append(line.lower())
    for otherwords in meow : 
        if str(otherwords).lower() in words :
            print(f"{str(otherwords)}" , end=" ")
        else :
            print(f"*{str(otherwords)}*" , end=" ")