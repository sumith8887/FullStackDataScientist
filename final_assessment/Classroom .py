class Student:
    def average_marks(self,students):
        average_marks_students={}
        avg=0
        for name,marks in students.items():
            avg=round(sum(marks)/len(marks),2)
            average_marks_students[name]=avg
        print("Average Marks: ",average_marks_students)
        top_avg=max(average_marks_students.values())
        top_students = [name for name, avg in average_marks_students.items() if avg == top_avg]
        if len(top_students) == 1:
            print("Top Performer:", top_students[0])
        else:
            print("Top Performers:", ", ".join(top_students))
student1=Student()
students_list=eval(input("Enter the list of student marks: "))
student1.average_marks(students_list)