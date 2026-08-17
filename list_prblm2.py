marks = [
    78, 85, 92, 67, 88,
    76, 95, 81, 73, 89,
    91, 64, 87, 79, 83,
    90, 72, 86, 75, 94
]


average = sum(marks) / len(marks)

print("Average marks:", average)


count = 0

for mark in marks:
    if mark > average:
        count += 1

print("Students scoring more than average:", count)


print("Maximum marks:", max(marks))