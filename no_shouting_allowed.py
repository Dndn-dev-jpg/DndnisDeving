# Write your solution here
def no_shouting(strings : list):
    meow = []
    for items in strings :
        if items.isupper() == True : 
            continue
        else : 
            meow.append(items)
    return meow 
