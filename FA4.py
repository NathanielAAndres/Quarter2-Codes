number_students = int(input("Enter the number of students: "))
number_subjects = int(input("Enter the number of subjects: "))

classtotal = 0

for student in range(1, number_students + 1):
    print("student", student)

    studenttotal = 0

    for subject in range(1, number_subjects + 1):
        grade = float(input("Enter grade for subject {}: ".format(subject)))
        studenttotal += grade

    studentaverage = studenttotal / number_subjects
    print("Average for student {}: {:.2f}".format(student, studentaverage))
    classtotal += studentaverage

    classaverage = classtotal / number_students
    print("Class Average: {:.2f}".format(classaverage))

