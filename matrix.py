# write your solution here
def read_matrix():
    with open("matrix.txt") as new_matrix :
        powper = []
        for number in new_matrix :
            powp = []
            number = number.replace("\n" , "")
            lister = number.split(",") 
            for num in lister :
                powp.append(int(num))
            powper.append(powp)
    return powper
def sum_rows() :
    powper = []
    meow = read_matrix()
    for row in meow : 
        powper.append(sum(row))
    return powper 
def matrix_sum():
    meow = sum_rows()
    return sum(meow)
def matrix_max():
    powper = []
    meow = read_matrix()
    for numbers in meow : 
        powper.append(max(numbers))
    return max(powper) 
def row_sums() :
    meow = sum_rows()
    return meow