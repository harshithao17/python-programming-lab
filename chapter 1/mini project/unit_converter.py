print("UNIT CONVERTER")

print("1. Kilometres to Metres")
print("2. Celsius to Fahrenheit")

choice = int(input("Enter your choice: "))

if choice == 1:
    km = float(input("Enter distance in kilometres: "))
    metres = km * 1000
    print("Distance in metres:", metres)

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

else:
    print("Invalid choice")