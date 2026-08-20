# Write your solution here
def list_of_stars(mylist : list) :
    for i in mylist : 
        stow = i * "*"
        print(stow) 
if __name__ == "__main__" : 
    list_of_stars([3, 7, 1, 1, 2])
    