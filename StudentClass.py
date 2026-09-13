class Student:
    def __init__(self, name, dept, roll):
        self.name = name
        self.dept = dept
        self.roll = roll

    def show(self):
        print(f"Roll No: {self.roll:<10} | Name: {self.name:<20} | Department: {self.dept}")


student1 = Student("Arjun Sharma", "Computer Science", 101)
student2 = Student("Priya Patel", "Electrical Eng.", 102)
student3 = Student("Rohan Verma", "Mechanical Eng.", 103)
student4 = Student("Ananya Das", "Civil Engineering", 104)
student5 = Student("Kabir Singh", "Information Tech.", 105)

student_list = [student1, student2, student3, student4, student5]

print("-" * 65)
print("                      STUDENT RECORDS                      ")
print("-" * 65)
for student in student_list:
    student.show()
print("-" * 65)

"""
OUTPUT:
-----------------------------------------------------------------
                      STUDENT RECORDS                      
-----------------------------------------------------------------
Roll No: 101        | Name: Arjun Sharma         | Department: Computer Science
Roll No: 102        | Name: Priya Patel          | Department: Electrical Eng.
Roll No: 103        | Name: Rohan Verma          | Department: Mechanical Eng.
Roll No: 104        | Name: Ananya Das           | Department: Civil Engineering
Roll No: 105        | Name: Kabir Singh          | Department: Information Tech.
-----------------------------------------------------------------
"""
