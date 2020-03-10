if __name__ == '__main__':
    names_grades = []

    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        names_grades.append([name,score])
        grades.append(score)

    max_grade = max(grades)
    min_grade = min(grades)
    students_with_secLowGrade = []
    for grade in range(len(grades)):
        if(grades[grade]>min_grade and grades[grade]<=max_grade):
            max_grade = grades[grade]

    for sec_lowG in range(len(names_grades)) :
        if(names_grades[sec_lowG][1] == max_grade):
            students_with_secLowGrade.append(names_grades[sec_lowG][0])
    students_with_secLowGrade.sort()

    print(*students_with_secLowGrade,sep="\n")
