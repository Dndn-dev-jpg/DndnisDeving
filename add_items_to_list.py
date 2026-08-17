# Write your solution here
times = int(input("How many items: "))
my_list = []
meower = 1
for _ in range(times) : 
    items = int(input(f"Item {meower}: "))
    my_list.append(items)
    meower += 1 
print(my_list)