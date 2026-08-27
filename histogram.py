# Write your solution here
def histogram(string : str): 
    dictionary = {}
    for letter in string : 
        if letter not in dictionary : 
            dictionary[letter] = []
        dictionary[letter].append(letter)
    for key , value in dictionary.items() : 
        print(f"{key} {len(value)*"*"}")
if __name__ == "__main__":
    histogram()


