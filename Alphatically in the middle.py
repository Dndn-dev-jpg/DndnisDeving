ltr1 = input("1st letter: ")
ltr2 = input("2nd letter: ")
ltr3 = input("3rd letter: ")
if ltr1 > ltr2 and ltr1 > ltr3 : 
    if ltr2 > ltr3 :
        print(f"The letter in the middle is {ltr2}")
    elif ltr3 > ltr2 :
        print(f"The letter in the middle is {ltr3}")
if ltr2 > ltr1 and ltr2 > ltr3 :
    if ltr1 > ltr3 : 
        print(f"The letter in the middle is {ltr1}")
    elif ltr3 > ltr1 : 
        print(f"The letter in the middle is {ltr3}")
if ltr3 > ltr1 and ltr3 > ltr2 :
    if ltr1 > ltr2 : 
        print(f"The letter in the middle is {ltr1}")
    elif ltr2 > ltr1 :
        print(f"The letter in the middle is {ltr2}")
    
print("Thank you for using this program!")