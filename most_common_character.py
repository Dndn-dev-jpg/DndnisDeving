# Write your solution here
def most_common_character(my_string: str):
    kowp = []
    peow = []
    for item in my_string : 
        meow = my_string.count(item)
        kowp.append(meow)
        peow.append(item)
    pesto = kowp.index(max(kowp))
    return peow[pesto]


if __name__ == "__main__":
    first_string = "edbdcba"
    print(most_common_character(first_string))
