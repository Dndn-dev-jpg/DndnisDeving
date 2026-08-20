# Write your solution here
def even_numbers(mylist : list):
    sumo = [] 
    for item in mylist : 
        if (item % 2) == 0 : 
            sumo.append(item)
    return sumo 
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)