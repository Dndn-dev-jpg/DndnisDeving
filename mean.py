# Write your solution here
def mean(mylist : list) : 
    length = len(mylist)
    sumo = sum(mylist)
    meano = sumo / length
    return meano
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print("mean value is", result)