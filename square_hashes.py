def line(length , string) : 
    if string == "" :
        string = "*"
    meow = length * (string[0])
    print(meow)

def square_of_hashes(size):
    cowaro = size
    for _ in range(size):
        line(cowaro, "#")
if __name__ == "__main__":
    square_of_hashes(5)