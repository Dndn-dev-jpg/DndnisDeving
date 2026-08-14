def line(length , string) : 
    if string == "" :
        string = "*"
    meow = length * (string[0])
    print(meow)

def box_of_hashes(height):
    while height > 0 :
        line(10, "#")
        height -= 1 
if __name__ == "__main__":
    box_of_hashes(5)
