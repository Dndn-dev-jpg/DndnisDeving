def exampointsandex(integer : int): 
    meow = integer.split()
    return meow
def roundingdown(meow : list):
    exam = int(meow[0])
    points = int((int(meow[1]) / 10))
    hello = exam + points
    return hello   
def makingthestars(hello : int):
    meow = "*" * hello
    return meow 
def main() :
    power = []
    kowp = []
    while True : 
        integer = input("Exam points and exercises completed: ")
        if integer == "":
            break
        helloer = exampointsandex(integer)
        kowp.append(int(helloer[1]))
        meow = roundingdown(helloer)
        power.append(meow)
    pointsaverage = float(sum(power) / len(power))
    stow = []
    index = 0
    for item in power : 
        if item >= 15 and int(item - int((kowp[index])/10) ) >= 10 :
            stow.append(item) 
        index += 1
    passpercentage = float((len(stow) / len(power))*100)
    print("Statistics:")
    print(f"Points average:{pointsaverage : .1f}")
    print(f"Pass percentage:{passpercentage : .1f}")
    print("Grade distribution:")
    listo = ["5: " , "4: " , "3: " , "2: " , "1: " , "0: "]
    grade = []
    indexroom = 0
    for grades in power : 
        if grades <= 14 or (grades - int((kowp[indexroom])/10)) < 10:
            grade.append(0)
        elif grades <= 17 : 
            grade.append(1)
        elif grades <= 20 : 
            grade.append(2)
        elif grades <= 23 : 
            grade.append(3)
        elif grades <= 27 :
            grade.append(4)
        elif grades <= 30 : 
            grade.append(5)
        indexroom +=1
    gra = 5
    for ranking in listo :
        print(f"{ranking}{makingthestars(grade.count(gra))}")
        gra -= 1
main()