attendance = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    status = input("Enter attendance (P/A): ").upper()

    while status not in ("P", "A"):
        print("Enter only P or A")
        status = input("Enter attendance (P/A): ").upper()

    attendance[name] = status

print("\nATTENDANCE REPORT")

present = 0
absent = 0

for name, status in attendance.items():

    if status == "P":
        print(name, "- Present")
        present += 1
    else:
        print(name, "- Absent")
        absent += 1

print("\nTotal Students:", n)
print("Present:", present)
print("Absent:", absent)