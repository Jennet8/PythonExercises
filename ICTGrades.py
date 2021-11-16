def grade(numbers):
    avg = sum(numbers)/175
    pcnt = avg*100
    return pcnt

def letter(x):
    if x > 80:
        y = "A"
    elif x > 70:
        y = "B"
    elif x > 60:
        y = "C"
    elif x > 50:
        y = "D"
    else:
         y = "F"
    return y

Student = str(input("Enter name: "))
HWScore = int(input("Homework score (/25):"))
AsScore = int(input("Assignment score (/50):"))
ExScore = int(input("Exam score (/100):"))

grades = [HWScore,AsScore,ExScore]

finalscore = grade(grades)
lettergrade = letter(finalscore)
print(f"{Student}'s final score is {finalscore}%. This is a grade of {lettergrade}.")