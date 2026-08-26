# Write your solution here
def print_sudoku(sudoku : list):
    power = 1
    makingspace = 0
    meow = "_"
    for item in sudoku :
        if makingspace in [3 , 6 , 9]:
            print()
        power = 1
        for kowp in item:
            if kowp == 0 :
                if power % 3 == 0 :
                    print(meow , end="  ")
                    power += 1
                    continue
                print(meow , end=" ")
                power += 1
            elif kowp != 0 and power % 3 == 0 :
                print(kowp , end="  ")
                power += 1
            elif kowp != 0 : 
                print(kowp , end=" ")
                power += 1
        print()
        makingspace +=1
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy = []
    index = 0
    while index < len(sudoku): 
        copy.append(sudoku[index][:])
        index += 1
    copy[row_no][column_no] = number
    return copy
if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)

