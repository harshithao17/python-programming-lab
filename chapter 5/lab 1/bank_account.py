class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Holder:", self.name)
        print("Available Balance:", self.balance)


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

print("\n1. Deposit")
print("2. Withdraw")
print("3. Display Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = float(input("Enter deposit amount: "))
    account.deposit(amount)

elif choice == 2:
    amount = float(input("Enter withdrawal amount: "))
    account.withdraw(amount)

elif choice == 3:
    account.display()

else:
    print("Invalid choice")

print("\nACCOUNT DETAILS")
account.display()