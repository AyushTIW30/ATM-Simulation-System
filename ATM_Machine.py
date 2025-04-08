class ATM:
    """
    A class to simulate basic ATM operations:
    - Create/change PIN
    - Check balance
    - Withdraw money
    """

    __counter = 1  # Class-level counter for customer IDs

    def __init__(self):
        """Initialize ATM instance with default PIN and balance."""
        self.pin = ""
        self.__balance = 0
        self.cid = ATM.__counter
        ATM.__counter += 1
        print(f"✅ ATM user {self.cid} created.")

    def get_counter(self):
        """Return the current value of the counter."""
        return ATM.__counter

    def set_counter(self, new_cid):
        """Set a new value for the counter if it's an integer."""
        if isinstance(new_cid, int):
            ATM.__counter = new_cid
            return "Counter updated."
        else:
            return "Not allowed. Counter must be an integer."

    def get_balance(self):
        """Return the current balance."""
        return self.__balance

    def set_balance(self, new_value):
        """Set a new balance if value is an integer."""
        if isinstance(new_value, int):
            self.__balance = new_value
        else:
            print("Access not granted.")

    def return_to_menu(self):
        """Ask user if they want to return to the menu."""
        choice = input("Enter 1 to go to the menu: ")
        if choice == "1":
            self.show_menu()

    def show_menu(self):
        """Display menu options for the user."""
        while True:
            user_input = input("""
------ ATM Menu ------
1. Create PIN
2. Change PIN
3. Check Balance
4. Withdraw Money
5. Exit
Enter your choice: """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.change_pin()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                self.withdraw()
            elif user_input == "5":
                print("🔒 Logged out of user session.\n")
                break
            else:
                print("❌ Invalid input. Try again.")

    def create_pin(self):
        """Create a new PIN and set the initial balance."""
        self.pin = input("Enter your new PIN: ")
        try:
            self.__balance = int(input("Enter initial balance: "))
            print("✅ PIN and balance set successfully.")
        except ValueError:
            print("❌ Invalid balance. Please enter a number.")

    def change_pin(self):
        """Change the existing PIN after verification."""
        old_pin = input("Enter your old PIN: ")
        if old_pin == self.pin:
            self.pin = input("Enter your new PIN: ")
            print("✅ PIN changed successfully.")
        else:
            print("❌ Incorrect PIN.")

    def check_balance(self):
        """Check account balance after PIN verification."""
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            print(f"💰 Your balance is ₹{self.__balance}")
        else:
            print("❌ Incorrect PIN.")

    def withdraw(self):
        """Withdraw money after PIN verification."""
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= self.__balance:
                    self.__balance -= amount
                    print(f"✅ Withdrawal successful. New balance: ₹{self.__balance}")
                else:
                    print("❌ Insufficient funds.")
            except ValueError:
                print("❌ Invalid amount.")
        else:
            print("❌ Incorrect PIN.")


# Multi-user logic
def main():
    users = {}

    while True:
        print("\n====== Welcome to the ATM System ======")
        print("1. Create New User")
        print("2. Login to Existing User")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user = ATM()
            users[user.cid] = user
            print(f"🎉 New user created with Customer ID: {user.cid}")

        elif choice == "2":
            try:
                cid = int(input("Enter your Customer ID: "))
                if cid in users:
                    users[cid].show_menu()
                else:
                    print("❌ User not found.")
            except ValueError:
                print("❌ Invalid Customer ID.")

        elif choice == "3":
            print("👋 Thank you for using the ATM. Goodbye!")
            break

        else:
            print("❌ Invalid input. Try again.")


if __name__ == "__main__":
    main()