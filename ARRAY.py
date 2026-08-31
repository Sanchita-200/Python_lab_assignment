
marks = [
    [45, 30, 90],
    [37, 57, 49],
    [90, 83, 95],
    [55, 65, 70],
    [45, 82, 80]
]


print("Maximum marks:", max(max(row) for row in marks))


print("Minimum marks:", min(min(row) for row in marks))


total = sum(sum(row) for row in marks)
average = total / 15

print("Average marks:", average)

subject1 = [row[0] for row in marks]
studentID = subject1.index(max(subject1))
print("4. Student ID with maximum marks in Subject 1:", studentID)


print("Maximum marks subject-wise:")

for j in range(3):
    maximum = max(marks[i][j] for i in range(5))
    print("Subject", j + 1, ":", maximum)


print("Average marks subject-wise:")

for j in range(3):
    total = sum(marks[i][j] for i in range(5))
    average = total / 5
    print("Subject", j + 1, ":", average)


for i in range(5):
    if marks[i][0]<50:
        marks[i][0]+=10

print("Marks after adding 10 marks",marks)

count=0
for i in range(5):
    if marks[i][2]>80:
        count+=1

print("no. of students score more than 80 in subject 2 is: ", count)


print("Minimum marks of student 2 : ",min(marks[2]))

print("Maximum marks of student 4 : ",max(marks[4]))


