#code tells odd or even 
number = int(input("Put in your number and let us decide: "))
if number >= 0:
    if number % 2 == 0:
        print(f"your number {number} is even and positive")
    else : 
        print(f"your number {number} is odd and positive")
elif number < 0 and number % 2 == 0 :
    print("your number is negative and even")
else : 
    print("your number is negative and odd")