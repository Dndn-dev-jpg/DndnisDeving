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
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no]= number
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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)