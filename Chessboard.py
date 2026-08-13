#im really proud of myself for making this , it made me struggle so much , but i won :
def chessboard (length):  
    meow = "" 
    x = 1
    accumlator = length
    while length > 0 :
        meow=""
        while len(meow) < accumlator :
            if x == 0 : 
                meow += f"{0}"
                if len(meow) == accumlator :
                    break
                meow += f"{1}"
            else : 
                meow += f"{1}"
                if len(meow) == accumlator :
                    break
                meow += f"{0}"  
        print(meow)
        if meow[0] == "1" : 
            x = 0
        if meow[0] == "0" :
            x = 1
        length -= 1 
if __name__ == "__main__":
    chessboard(6)
