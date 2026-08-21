# Write your solution here
def longest_series_of_neighbours(mylist : list):
    index = 0 
    current = 1
    remember = 1
    while index <= (len(mylist) - 2) :
        if (mylist[index + 1] - mylist[index]) in [-1 , 1] :
            current += 1 
        else : 
            current = 1
        if current > remember :
            remember = current
        index += 1
    return remember
    
    
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]  #input any list you want ,
    print(longest_series_of_neighbours(my_list)) #make sure to put numbers
                                                 #that difference between them -1 or 1 
                                                 #so you can get a streak