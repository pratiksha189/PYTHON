class Students:
    def __init__(self,roll_no , student_name,marks):
        self.roll_no = roll_no
        self.student_name = student_name
        self.marks = marks

    def __str__(self):
        return (f'{self.roll_no},{self.student_name}')

    def calculate_gpa(self):
        m1,m2,m3 = self.marks
        gpa=(1/3)*m1+(1/2)*m2+(1/4)*m3
        return gpa

student = [Students(1,"Anushka",[70,80,90]),
Students(2,"Bhaskar",[80,50,90]),
Students(3,"Ashish",[10,20,30]),
Students(4,"Dikshit",[50,45,67]),
Students(5,"Elephant",[46,76,65])]

## give roll no. and it will print gpa
roll_no = int(input("Enter roll number: "))
## op = [print(f"GPA of {i}= {i.calculate_gpa()}") for i in student if i.roll_no==roll_no] # list comprehension:
# for s in student:
#         if s.roll_no==roll_no:
#             print(s)
#             print(f"GPA = {s.calculate_gpa()}")

## in order to display all students
# for i in student:
#     print(f"student = {i.student_name},GPA = {i.calculate_gpa()}")








'''
Q1. Create a class 'Student' with rollno, studentName, dictionary/list of marks 
(subjectName -> marks [3]) /marks[3].
Provide following functionalities
A. initializer (init)
B. implement_str method
C. Print student data for given id.
D. Calculate GPA()
gpa=(1/3)*m1+(1/2)*m2+(1/4)*m3
# -----------------------------------------------------------------------------

Create 5 student objects and store them in a list
For the student data stored in the list perform following operation:
1. Display All Student
2. Search by id
3. Sort by name
4. Calculate GPA of a student
'''