grades_list=list(map(int,input("Enter the Student grades : ").split()))
grade_marks=sum(grades_list)/len(grades_list)

if(grade_marks<=100 and grade_marks>90):
    print("S grade")
elif(grade_marks<=90 and grade_marks>80):
    print("A+ grade")
elif(grade_marks<=80 and grade_marks>70):
    print("A grade")
elif(grade_marks<=70 and grade_marks>60):
    print("B+ grade")
elif(grade_marks<=60 and grade_marks>50):
    print("B grade")
elif(grade_marks<=50 and grade_marks>40):
    print("Pass")
else:
    print("Fail")