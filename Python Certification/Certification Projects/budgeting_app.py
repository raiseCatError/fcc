class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        if description:
            return(f"Deposited {amount}$ for {self.name},\nDescription: {description}")
            
        else:
            return(f"Deposited {amount}$ for {self.name}")
            

    def get_balance(self):
        actual_balance = 0
        for et in self.ledger:
            actual_balance += et['amount']
        return actual_balance
        

    def withdraw(self, amount, description=''):
        balance = self.check_funds(amount)
        if balance == True:
            self.ledger.append({'amount': -amount, 'description': description})
            if description:
                print(f"Withdrawn {amount}$ for {self.name},\nDescription: {description}")
            else:
                print(f"Withdrawn {amount}$ for {self.name}")
            return True
        else:
            print(f"Transaction Failed, Insufficient Funds!\n{balance}")
            return False

    def transfer(self, amount, destination, description=''):
        balance = self.check_funds(amount)
        if balance == True:
            self.withdraw(amount, description=f'Transfer to {destination.name}')
            destination.deposit(amount, description =f"Transfer from {self.name}")
            return True
        else:         
            print(f"Transfer Failed, Insufficient Funds!\n{balance}")
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

    def __str__(self):
        output = self.name.center(30, '*') + '\n'

        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"
            output += f"{description:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output


food = Category('Food')
print(food.deposit(50, ''))
print(food.withdraw(20, ''))
print("-------")
clothing = Category('Clothing')
print(clothing.deposit(300, ''))
print(clothing.withdraw(200, ''))
print("-------")

print(food.get_balance())
print(clothing.get_balance())

print(food.transfer(10, clothing))

print(food)




def create_spend_chart(categories):
    # Calculate total spending
    total_spent = 0
    category_spending = []

    for category in categories:
        spent = 0

        for item in category.ledger:
            if item['amount'] < 0:
                spent += -item['amount']

        category_spending.append(spent)
        total_spent += spent

    # Calculate percentages, rounded down to nearest 10
    percentages = []

    for spent in category_spending:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int(spent / total_spent * 100 // 10 * 10)

        percentages.append(percentage)

    # Build chart
    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        chart += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        chart += "\n"

    return chart.rstrip("\n")