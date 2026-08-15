def spruce(size) :
    star = "*"
    meow = 1
    adding = " "
    longer = size - 1
    print("a spruce!")
    while (size * 2) >= meow :
        kower = longer * adding + star * meow
        print(kower)
        longer -= 1
        meow += 2
    print((size - 1)*adding + star)
if __name__ == "__main__":
    spruce(3)