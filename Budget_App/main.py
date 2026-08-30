class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Appends a dictionary object containing amount and description
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # Uses check_funds to verify availability before proceeding
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        # Calculates the sum of all deposits and withdrawals
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category_instance):
        # Conditional transfer based on fund availability
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        # Returns False if amount exceeds balance, True otherwise
        return amount <= self.get_balance()

    def __str__(self):
        # 1. Generate centered title line (30 characters long)
        title = self.name.center(30, "*") + "\n"
        
        # 2. Format and add ledger entries
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]  # Truncate to max 23 chars
            amt = f"{item['amount']:.2f}"   # Format to 2 decimal places
            items += f"{desc:<23}{amt:>7}\n" # Left-align description, right-align amount
            
        # 3. Add total balance line
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # 1. Calculate withdrawals per category and total overall spending
    spendings = []
    for cat in categories:
        spend = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spendings.append(spend)
        
    total_spent = sum(spendings)
    
    # 2. Calculate percentages rounded down to nearest 10
    # Handle division by zero case safely if there is no spending at all
    percentages = []
    for s in spendings:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((s / total_spent) * 100 // 10) * 10)

    # 3. Build the graph bars from 100 down to 0
    chart = "Percentage spent by category\n"
    for r in range(100, -1, -10):
        chart += f"{r:>3}|"
        for p in percentages:
            if p >= r:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"  # Spacing logic requires 1 final space after the bars + newline

    # 4. Draw the horizontal line divider
    # 3 dashes per category + 1 initial dash + 1 trailing dash
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 5. Arrange names vertically
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        chart += "    "
        for name in names:
            chart += f" {name[i]} "
        chart += " "  # Spacing logic requires 1 final trailing space
        if i < max_len - 1:
            chart += "\n"  # Final line must not have a trailing newline

    return chart
