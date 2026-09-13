"""
Question - Create a 2D array to store the marks of 3 subjects of 5 students.
Now perform the following operations on the marks array.
1. Maximum Marks
2. Minimum Marks
3. Average Marks
4. Find the studentID (0 to 5) who score maximum marks in subject1.
5. Find maximum marks subject-wise.
6. Find the average marks subject-wise.
7. Add 10 marks for all students whose score is less than 50 in subject1.
8. Find out number of students who scored more than 80 in subject 2.
9. Find out the minimum marks of student2.
10. Find out the maximum marks of the student4.
"""
import numpy as np

marks = np.array([
    [95, 67, 82],
    [75, 44, 73],
    [90, 32, 88],
    [45, 84, 89],
    [62, 99, 77]
])

print("1. Maximum Marks:", np.max(marks))

print("2. Minimum Marks:", np.min(marks))

print("3. Average Marks:", np.mean(marks))

print("4. StudentID with maximum marks in subject1:", np.argmax(marks[:, 0]))

print("5. Maximum marks subject-wise:", np.max(marks, axis=0))

print("6. Average marks subject-wise:", np.mean(marks, axis=0))

marks[:, 0] = np.where(marks[:, 0] < 50, marks[:, 0] + 10, marks[:, 0])
print("7. Array after adding 10 marks to subject1 < 50:\n", marks)

print("8. Number of students scoring > 80 in subject 2:", np.sum(marks[:, 1] > 80))

print("9. Minimum marks of student2:", np.min(marks[2, :]))

print("10. Maximum marks of student4:", np.max(marks[4, :]))
