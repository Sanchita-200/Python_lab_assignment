employees = (
    "Rahul", "Amit", "Priya", "Rahul", "Riya",
    "Amit", "Karan", "Sneha", "Priya", "Rahul",
    "Neha", "Rohan", "Amit", "Karan", "Priya",
    "Sneha", "Rahul", "Neha", "Amit", "Riya"
)


print("Name and Frequency:")

for name in set(employees):
    print(name, ":", employees.count(name))


unique_names = set(employees)

print("\nDistinct names:", unique_names)
print("Number of distinct names:", len(unique_names))


max_frequency = 0
max_name = ""

for name in unique_names:
    frequency = employees.count(name)

    if frequency > max_frequency:
        max_frequency = frequency
        max_name = name

print("\nName with maximum frequency:", max_name)
print("Frequency:", max_frequency)


sorted_names = sorted(employees)

print("\nAlphabetical order:")
print(sorted_names)


search = input("\nEnter employee name: ")

if search in employees:
    print("Employee exists in the tuple.")
else:
    print("Employee does not exist.")