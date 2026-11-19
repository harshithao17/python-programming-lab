import csv

with open("payroll.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Employee Name",
        "Basic Salary",
        "Allowance",
        "Deduction",
        "Net Salary"
    ])

    n = int(input("Enter number of employees: "))

    for i in range(n):

        name = input("Enter employee name: ")
        basic = float(input("Enter basic salary: "))
        allowance = float(input("Enter allowance: "))
        deduction = float(input("Enter deduction: "))

        net_salary = basic + allowance - deduction

        writer.writerow([
            name, basic, allowance,
            deduction, net_salary
        ])

print("\nPAYROLL DETAILS")

with open("payroll.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)