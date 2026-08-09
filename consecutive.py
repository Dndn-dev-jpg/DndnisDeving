limit = int(input("Limit: "))
expression = "" 
total = 1
add_to_exp = 0
while limit > add_to_exp :
    add_to_exp += total
    if expression == "":
        expression = f"{total}"
    else:
        expression += f" + {total}"
    total += 1
print(f"The consecutive sum: {expression} = {add_to_exp}")
