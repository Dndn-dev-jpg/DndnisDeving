year = int(input("Year: "))
original = year
year += 1
while True:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"The next leap year after {original} is {year}")
        break
    year += 1