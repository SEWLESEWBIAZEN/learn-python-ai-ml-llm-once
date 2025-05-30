
class Account:    
    def __init__(self, account_holder=None, balance=0.0):
        """
        Initialize an account with optional account holder name and balance.
        Default balance is 0.0 if not provided.
        """
        self.account_holder = account_holder
        self.balance = balance

    def create_account(self):
        """Creates a new account by taking user input for account details."""
        print("\n--- Create New Account ---")
        self.account_holder = input("Enter account holder name: ").strip()
        
        while True:
            try:
                balance = float(input("Enter initial balance: "))
                if balance < 0:
                    print("Balance cannot be negative. Please try again.")
                    continue
                self.balance = balance
                print(f"Account created successfully for {self.account_holder} with balance ${self.balance:.2f}")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for balance.")

    def deposit_to_account(self):
        """Deposits money into the account after verifying account holder."""
        print("\n--- Deposit Money ---")
        name = input("Enter the account holder name: ").strip()
        
        if name != self.account_holder:
            print("Error: Account holder name doesn't match.")
            return
            
        while True:
            try:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    print("Deposit amount must be positive.")
                    continue
                self.balance += amount
                print(f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def withdraw_from_account(self):
        """Withdraws money from the account if sufficient balance exists."""
        print("\n--- Withdraw Money ---")
        name = input("Enter the account holder name: ").strip()
        
        if name != self.account_holder:
            print("Error: Account holder name doesn't match.")
            return
            
        while True:
            try:
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Withdrawal amount must be positive.")
                    continue
                if amount > self.balance:
                    print("Insufficient funds for this withdrawal.")
                    continue
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def check_balance(self):
        """Displays the current account balance."""
        print("\n--- Account Balance ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")

    def account_menu(self):
        """Provides an interactive menu for account operations."""
        while True:
            print("\n===== Account Menu =====")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                self.create_account()
            elif choice == '2':
                if not self.account_holder:
                    print("Please create an account first.")
                    continue
                self.deposit_to_account()
            elif choice == '3':
                if not self.account_holder:
                    print("Please create an account first.")
                    continue
                self.withdraw_from_account()
            elif choice == '4':
                if not self.account_holder:
                    print("Please create an account first.")
                    continue
                self.check_balance()
            elif choice == '5':
                print("Thank you for using our banking system!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")


# Example usage
if __name__ == "__main__":
    account = Account()
    account.account_menu()
