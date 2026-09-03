def get_marks():
    eng = int(input("English:"))
    math = int(input("Maths:"))
    sci = int(input("Science:"))
    soc = int(input("Social:"))
    com = int(input("Computer:"))
    return[eng, math, sci,soc, com]

def calculate_total(marks):
    return sum(marks)

def calculate_average(total):
    return total/5

def find_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"

def display_result(total,avg,grade):
    if avg >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    print("\nOutput:")
    print("Total marks:", total)
    print("Average:",int(avg))
    print("Grade:", grade)
    print("Result:", result)

marks = get_marks()
total = calculate_total(marks)
avg = calculate_average(total)
grade = find_grade(avg)
display_result(total,avg,grade)
