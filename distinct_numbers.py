def distinct_numbers(listo : list) : 
    powp = []
    for item in listo : 
        if item in powp : 
            continue
        powp.append(item) 
    powp.sort()
    return powp
if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) 