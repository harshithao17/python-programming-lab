print("SIMPLE CALCULATOR")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")

print("\nAREA CALCULATION")

length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))

print("Area of Rectangle:", length * breadth)

radius = float(input("Enter circle radius: "))

area = 3.14 * radius * radius

print("Area of Circle:", area)