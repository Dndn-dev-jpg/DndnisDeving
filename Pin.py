tries = 0
while True:
    pin = int(input("PIN: "))
    tries += 1

    if pin == 4321:
        if tries == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {tries} attempts")
        break

    print("Wrong")

    if tries >= 4:
        print("Too many attempts...")
        break