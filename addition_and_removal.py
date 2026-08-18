# Write your solution here
addition = 1
index = 0
meow = [] #'d', 'r', 'd', 'd', 'd', 'r', 'r', 'x'
while True : 
    kow = print(f"The list is now {meow}")
    value = input("a(d)d, (r)emove or e(x)it: ")
    if value == "x" :
        print("Bye!") 
        break
    if value == "d" : 
        meow.insert(index , addition)
        addition += 1
        index += 1
    if value == "r" : 
        meow.pop(-1)
        addition -= 1
        index -= 1
    
  