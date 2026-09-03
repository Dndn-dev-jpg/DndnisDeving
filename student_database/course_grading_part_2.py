# write your solution here
studentinfo = input("Student information: ")
pointsofexc = input("Exercises completed: ")
exampoints = input("Exam points: ")
def grader(exc : int , exam : int) : 
    grado = exc // 4 + exam
    if grado <= 14 :
        return 0
    elif 15 <= grado <= 17 :
        return 1 
    elif 18 <= grado <= 20 :
        return 2
    elif 21 <= grado <= 23 :
        return 3 
    elif 24 <= grado <= 27 :
        return 4
    elif 28 <= grado :
        return 5
students = {}
with open(f"{studentinfo}") as new_students :
    for line in new_students : 
        line = line.replace("\n" , "")
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else : 
            students[parts[0]] = f"{parts[1]} {parts[2]}" 
excercice = {}
with open(f"{pointsofexc}") as new_exc : 
    for lines in new_exc :
        index = 0
        lines = lines.replace("\n" , "")
        parto = lines.split(";")
        if parto[0] == "id":
            continue
        else :
            for number in parto[1 : ] :
                index += int(number)
            excercice[parto[0]] = index
exams = {}
with open(f"{exampoints}") as new_exams : 
    for lino in new_exams :
        grade = 0 
        lino = lino.replace("\n" , "")
        party = lino.split(";")
        if party[0] == "id" :
            continue
        else : 
            for grades in party[1 : ]:
                grade += int(grades)
            exams[party[0]] = grade
for key , names in students.items():
    if key in excercice and key in exams : 
        print(f"{students[key]} {grader((excercice[key]) , exams[key])}")
    else :
        print("this isn't in our database")

    

