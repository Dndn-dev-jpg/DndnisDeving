while True :
    number = int(input("Please type in a number: "))
    powy = number
    factorial = 1
    if number <= 0 :
        print("Thanks and bye!")
        break
    while number >= 1 :
        factorial *= number 
        number -= 1
    print(f"The factorial of the number {powy} is {factorial}")