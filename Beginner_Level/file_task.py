import csv

students = [
    ["Name", "Math", "Science", "English"],
    ["Ravi", 80, 85, 90],
    ["Anita", 70, 75, 80],
    ["John", 60, 65, 70]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

for i in range(1, len(data)):
    marks = list(map(int, data[i][1:]))
    total = sum(marks)
    avg = total / len(marks)
    print(data[i][0], total, avg)
