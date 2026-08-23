# Write your solution here
def longest(strings: list):
    poew = 0
    index = []
    for item in strings : 
        meow = len(item)
        if meow > poew : 
            poew = meow 
            index.append(item)
    return index[-1] 
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))