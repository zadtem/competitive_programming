
def gradingStudents(grades):
    rounded_grade = []
    for grade in grades:
        if (grade//5 + 1)*5 - grade < 3 and (grade//5 + 1)*5 >= 40:
            rounded_grade.append((grade//5 + 1)*5)
        elif (grade//5 + 1)*5 - grade >= 3 and (grade//5 + 1)*5 >= 40 or grade< 35:
            rounded_grade.append(grade)
    return rounded_grade