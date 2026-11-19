file = open("students.txt", "w")

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    file.write(name + "," + roll + "\n")

file.close()

# Reading student details

file = open("students.txt", "r")

print("\nSTUDENT DETAILS")

for line in file:
    name, roll = line.strip().split(",")
    print("Name:", name)
    print("Roll Number:", roll)
    print("----------------")

file.close()