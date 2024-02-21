#heading
print("\t\tBIT EVENING SSTUDENTS SCORE")
print("\n")
print("\tPlease fill in as instructed below")
print("\n")

#students data
student_name = str(input("Please enter studnt's name: \n"))
reg_no = str(input("please enter Reg N0 for student \n"))
course_work = int(input("enter course wrk marks\n"))
zz
if course_work <101:
    students_exam = int(input("Enter student's score\n"))
else:
    print("invalid input")
    print("\n")


#calculations
first = course_work * float(0.3)
second = students_exam * float(0.7)
final_score = first + int(second)
print(f"course work marks is: {first}, and exam marks is: {second}")
print(final_score)

if final_score < 50:
    print("Repeat")
else:
    print("passed")

    score_out_70 = int(students_exam/100) * 70
    score_out_30 = int(course_work/100) * 30