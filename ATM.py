class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have deposited ${amount}. Your new balance is: ${self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"You have withdrawn ${amount}. Your new balance is: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount entered!")

def main():
    atm = ATM(100)  # Starting balance

    while True:
        print("\nWelcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Please choose an option: "))

            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
