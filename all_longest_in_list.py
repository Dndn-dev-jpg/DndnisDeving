# Write your solution here
def all_the_longest(mylist : list):
    meow = []
    steamer = []
    index = 0
    for item in mylist : 
        meow.append(len(item))
    for stem in meow :
        if stem == max(meow) :
            hellothere = meow.index(stem , index)
            steamer.append(mylist[hellothere])
            index = hellothere + 1
    return steamer 
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
    

