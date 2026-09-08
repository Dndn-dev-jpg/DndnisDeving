# Write your solution here
while True : 
        print("1 - add an entry, 2 - read entries, 0 - quit")
        meow = int(input("Function: "))
        if meow == 0 :
            print("Bye now!")
            break
        elif meow == 1 :
            with open("diary.txt" , "a") as new_file :
                entry = input("Diary entry: ")
                new_file.write(f"{entry}\n")
                print("Diary saved")
        if meow == 2 :
            with open("diary.txt") as new_file :
                print("Entries:")
                for lines in new_file :
                    lines = lines.replace("\n" , "")
                    print(lines)
            