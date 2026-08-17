class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = float(amount)
        self.category = category

    def display(self):
        print(f"  {self.name} | ${self.amount} | {self.category}")
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, category):
        expense = Expense(name, amount, category)
        self.expenses.append(expense)
        print(f"Added: {name}")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses yet.")
        else:
            print("\n--- All Expenses ---")
            for i, expense in enumerate(self.expenses):
                print(f"{i+1}.", end="")
                expense.display()

    def view_total(self):
        total = sum(e.amount for e in self.expenses)
        print(f"\nTotal spent: ${total:.2f}")

    def delete_expense(self, index):
        if index < 1 or index > len(self.expenses):
            print("Invalid number.")
        else:
            removed = self.expenses.pop(index - 1)
            print(f"Deleted: {removed.name}")


# Test it
def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("\nChoose (1-5): ")

        if choice == "1":
            name = input("Expense name: ")
            amount = input("Amount: ")
            category = input("Category (Food/Transport/Other): ")
            tracker.add_expense(name, amount, category)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            tracker.view_total()

        elif choice == "4":
            tracker.view_expenses()
            index = int(input("Enter number to delete: "))
            tracker.delete_expense(index)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1-5.")

main()