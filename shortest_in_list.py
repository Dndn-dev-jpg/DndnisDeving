# Write your solution here
def shortest(mylist : list): 
    powow = []
    for item in mylist : 
        powow.append(len(item))
    meow = powow.index(min(powow))
    steamer = mylist[meow]
    return steamer
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)