class Student:

    def __init__(self, name, department, roll):
        self.name = name
        self.department = department
        self.roll = roll

    def show(self):
        print("Name:", self.name)
        print("Department:", self.department)
        print("Roll:", self.roll)
        print()


student1 = Student("Rahul", "CSE", 101)
student2 = Student("Priya", "CSE", 102)
student3 = Student("Amit", "ECE", 103)
student4 = Student("Riya", "IT", 104)
student5 = Student("Sneha", "CSE", 105)

student1.show()
student2.show()
student3.show()
student4.show()
student5.show()