# Write your solution here
def everything_reversed(mylist : list): 
    meow = mylist[::-1]
    peow = []
    for item in meow : 
        peow.append(item[::-1])
    return peow
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
