import tkinter as tk
from tkinter import messagebox
import connnect_mongo_db as connect

# Connect to MongoDB
db_connection = connect.MongoDBConnection()
[accounts_col, transactions_col] = db_connection.connect_to_mongo()

class ATMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ATM Machine with MongoDB")
        self.geometry("1000x800")        
        self.current_user = None
        self.container = tk.Frame(self, bg="lightgray", padx=20, pady=20)
        self.container.pack(fill="both", expand=True)
        self.frames = {}
        self.container.config(bg="lightgray")
        self.container.pack_propagate(False)  # Prevent the container from resizing to fit its children
      

        for F in (HomeScreen, CreateAccount, LoginScreen, DepositScreen,
                  WithdrawScreen, CheckBalanceScreen, ChangePINScreen,
                  TransactionHistoryScreen, AdminScreen):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame(HomeScreen)

    def show_frame(self, screen):
        self.frames[screen].tkraise()

class CustomButton(tk.Button):
    
    def create_button(self,parent, text, command=None):
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 12),
            bg="lightblue",           
            width=20,
            padx=10,
            pady=5
        )



class HomeScreen(tk.Frame):    
    
    def __init__(self, parent, controller):
        cb = CustomButton()
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="ATM Main Menu", font=("Arial", 18)).pack(pady=10)

        # Create a centered container frame for the buttons
        button_container = tk.Frame(self)
        button_container.pack(pady=20)

        # Horizontally aligned buttons inside the container
        cb.create_button(button_container, "Create Account", command=lambda: controller.show_frame(CreateAccount)).pack(side='left', padx=10)
        cb.create_button(button_container, "Login", command=lambda: controller.show_frame(LoginScreen)).pack(side='left', padx=10)
        cb.create_button(button_container, "Admin Panel", command=lambda: controller.show_frame(AdminScreen)).pack(side='left', padx=10)
        cb.create_button(button_container, "Exit", command=controller.destroy).pack(side='left', padx=10)
        # Add a label for the welcome message
        # Alternative button creation

class CreateAccount(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Create Account", font=("Arial", 18)).pack(pady=10)
        self.name = tk.Entry(self)
        self.pin = tk.Entry(self, show="*")
        self.balance = tk.Entry(self)
        for label, entry in [("Name", self.name), ("PIN", self.pin), ("Initial Deposit", self.balance)]:
            tk.Label(self, text=label).pack()
            entry.pack()
        tk.Button(self, text="Create", command=self.create_account).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(HomeScreen)).pack()

    def create_account(self):
        name, pin, balance = self.name.get(), self.pin.get(), self.balance.get()
        if accounts_col.find_one({"name": name}):
            messagebox.showerror("Error", "Account already exists.")
        elif not pin.isdigit() or len(pin) != 4:
            messagebox.showerror("Error", "PIN must be 4 digits.")
        elif not balance.isdigit():
            messagebox.showerror("Error", "Invalid amount.")
        else:
            accounts_col.insert_one({"name": name, "pin": pin, "balance": int(balance)})
            messagebox.showinfo("Success", "Account created.")
            self.controller.show_frame(HomeScreen)


class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Login", font=("Arial", 18)).pack(pady=10)
        self.name = tk.Entry(self)
        self.pin = tk.Entry(self, show="*")
        for label, entry in [("Name", self.name), ("PIN", self.pin)]:
            tk.Label(self, text=label).pack()
            entry.pack()
        tk.Button(self, text="Login", command=self.login).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(HomeScreen)).pack()

    def login(self):
        name, pin = self.name.get(), self.pin.get()
        user = accounts_col.find_one({"name": name, "pin": pin})
        if user:
            self.controller.current_user = user
            messagebox.showinfo("Welcome", f"Logged in as {name}")
            self.controller.show_frame(DepositScreen)
        else:
            messagebox.showerror("Error", "Invalid credentials")


class DepositScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Deposit", font=("Arial", 18)).pack(pady=10)
        self.amount = tk.Entry(self)
        tk.Label(self, text="Amount").pack()
        self.amount.pack()
        tk.Button(self, text="Deposit", command=self.deposit).pack(pady=5)
        self.add_nav_buttons()

    def deposit(self):
        amt = self.amount.get()
        user = self.controller.current_user
        if amt.isdigit():
            new_balance = user["balance"] + int(amt)
            accounts_col.update_one({"_id": user["_id"]}, {"$set": {"balance": new_balance}})
            transactions_col.insert_one({"user": user["name"], "type": "deposit", "amount": int(amt)})
            user["balance"] = new_balance
            messagebox.showinfo("Success", f"Deposited ${amt}")
        else:
            messagebox.showerror("Error", "Invalid amount.")

    def add_nav_buttons(self):
        tk.Button(self, text="Withdraw", command=lambda: self.controller.show_frame(WithdrawScreen)).pack()
        tk.Button(self, text="Check Balance", command=lambda: self.controller.show_frame(CheckBalanceScreen)).pack()
        tk.Button(self, text="Change PIN", command=lambda: self.controller.show_frame(ChangePINScreen)).pack()
        tk.Button(self, text="Transaction History", command=lambda: self.controller.show_frame(TransactionHistoryScreen)).pack()
        tk.Button(self, text="Logout", command=self.logout).pack(pady=5)

    def logout(self):
        self.controller.current_user = None
        self.controller.show_frame(HomeScreen)


class WithdrawScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Withdraw", font=("Arial", 18)).pack(pady=10)
        self.amount = tk.Entry(self)
        tk.Label(self, text="Amount").pack()
        self.amount.pack()
        tk.Button(self, text="Withdraw", command=self.withdraw).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(DepositScreen)).pack()

    def withdraw(self):
        amt = self.amount.get()
        user = self.controller.current_user
        if amt.isdigit() and int(amt) <= user["balance"]:
            new_balance = user["balance"] - int(amt)
            accounts_col.update_one({"_id": user["_id"]}, {"$set": {"balance": new_balance}})
            transactions_col.insert_one({"user": user["name"], "type": "withdraw", "amount": int(amt)})
            user["balance"] = new_balance
            messagebox.showinfo("Success", f"Withdrew ${amt}")
        else:
            messagebox.showerror("Error", "Invalid amount or insufficient funds.")


class CheckBalanceScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.balance_label = tk.Label(self, text="", font=("Arial", 18))
        self.balance_label.pack(pady=20)
        tk.Button(self, text="Refresh", command=self.refresh_balance).pack()
        tk.Button(self, text="Back", command=lambda: controller.show_frame(DepositScreen)).pack()

    def refresh_balance(self):
        user = self.controller.current_user
        fresh = accounts_col.find_one({"_id": user["_id"]})
        if fresh:
            self.controller.current_user = fresh
            self.balance_label.config(text=f"Balance: ${fresh['balance']}")
        else:
            messagebox.showerror("Error", "Account not found.")


class ChangePINScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Change PIN", font=("Arial", 18)).pack(pady=10)
        self.new_pin = tk.Entry(self, show="*")
        tk.Label(self, text="New PIN (4 digits)").pack()
        self.new_pin.pack()
        tk.Button(self, text="Change", command=self.change_pin).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(DepositScreen)).pack()

    def change_pin(self):
        user = self.controller.current_user
        pin = self.new_pin.get()
        if pin.isdigit() and len(pin) == 4:
            accounts_col.update_one({"_id": user["_id"]}, {"$set": {"pin": pin}})
            user["pin"] = pin
            messagebox.showinfo("Success", "PIN changed.")
        else:
            messagebox.showerror("Error", "PIN must be 4 digits.")


class TransactionHistoryScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.history_text = tk.Text(self, height=15, width=45)
        tk.Label(self, text="Transaction History", font=("Arial", 18)).pack(pady=10)
        self.history_text.pack()
        tk.Button(self, text="Load History", command=self.load_history).pack()
        tk.Button(self, text="Back", command=lambda: controller.show_frame(DepositScreen)).pack(pady=5)

    def load_history(self):
        self.history_text.delete("1.0", tk.END)
        user = self.controller.current_user
        history = transactions_col.find({"user": user["name"]}).sort("_id", -1)
        for item in history:
            self.history_text.insert(tk.END, f"{item['type'].capitalize()} ${item['amount']}\n")


class AdminScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        tk.Label(self, text="Admin Panel", font=("Arial", 18)).pack(pady=10)
        tk.Label(self, text="Username to delete:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        tk.Button(self, text="Delete User", command=self.delete_user).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(HomeScreen)).pack()

    def delete_user(self):
        name = self.username_entry.get()
        result = accounts_col.delete_one({"name": name})
        transactions_col.delete_many({"user": name})
        if result.deleted_count > 0:
            messagebox.showinfo("Deleted", f"User '{name}' deleted.")
        else:
            messagebox.showerror("Error", "User not found.")


if __name__ == "__main__":
    app = ATMApp()
    app.mainloop()
    

