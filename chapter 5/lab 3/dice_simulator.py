import random

print("DICE SIMULATOR")

while True:

    choice = input("Press R to roll the dice or Q to quit: ").upper()

    if choice == "R":
        dice = random.randint(1, 6)
        print("Dice Number:", dice)

    elif choice == "Q":
        print("Game ended")
        break

    else:
        print("Invalid choice")