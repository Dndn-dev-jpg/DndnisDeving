def add_student(students : dict , person : str):
    students[person] = []
def print_student (students : dict , person : str):
    mean = []
    if person not in students : 
        print(f"{person}: no such person in the database")
    elif students[person] == [] :
        print(f"{person}:")
        print(" no completed courses")
    else :
        print(f"{person}:")
        print(f" {len(students[person])} completed courses:")
        for items in students[person]:
            print(f"  {items[0]} {items[1]}")
            mean.append(items[1])
        print(f" average grade {(sum(mean) / len(mean))}")   
def add_course(students : dict , person : str , coursedata : tuple): 
    programs = []     
    for program in students[person] :         
        programs.append(program[0])     
    if coursedata[0] not in programs and coursedata[1] >= 1 :             
        students[person].append(coursedata)
    elif coursedata[0] in programs :
        for programso , grades in enumerate(students[person]) :
            if grades[0] == coursedata[0] and grades[1] <= coursedata[1]:
                students[person][programso] = coursedata
def summary(students : dict):
    previouscompleted = 0
    studento = 0
    powp = None
    iwon = 0
    finallo = ""
    for person , courses in students.items():
        if len(courses) > previouscompleted :
            previouscompleted = len(courses)
            meow = person
        studento += 1
    for student , grades in students.items():
        pew = 0
        for average in grades : 
            pew += average[1]
        powp = (pew / len(grades))
        if powp > iwon : 
            iwon = powp
            finallo = student
    print(f"students {studento}")
    print(f"most courses completed {previouscompleted} {meow}")
    print(f"best average grade {iwon} {finallo}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)
