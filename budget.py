class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        # title
        catLen = len(self.category)
        titleLen = 30 - catLen
        titleMid = round(titleLen / 2)
        title = ("*" * titleMid) + self.category + \
            ("*" * (titleLen - titleMid)) + "\n"

        # transactions
        transactions = ''
        for transaction in self.ledger:
            newDesc = transaction['description']
            newAmt = str(transaction['amount'])
            decimal = newAmt.find('.')

            if (decimal == -1):
                newAmt += '.00'

            descLen = len(newDesc)
            amtLen = len(newAmt)
            spaceLen = 30 - descLen - amtLen

            if (descLen + amtLen >= 30):
                diff = 30 - (descLen + amtLen + 1)
                newDesc = newDesc[:diff]
                spaceLen = 1

            spaces = spaceLen * " "
            transactions += newDesc + spaces + newAmt + "\n"

        # total
        total = 'Total: ' + str(self.get_balance())

        return title + transactions + total

    def deposit(self, amt, desc=''):
        self.ledger.append({"amount": amt, "description": desc})

    def withdraw(self, amt, desc=''):
        haveFunds = self.check_funds(amt)

        if (haveFunds):
            self.ledger.append({"amount": -abs(amt), "description": desc})
            return True

        return False

    def get_balance(self):
        balance = 0

        for transaction in self.ledger:
            balance += float(transaction['amount'])

        return balance

    def transfer(self, amt, category):
        success = self.withdraw(amt, "Transfer to " + category.category)

        if (success):
            category.deposit(amt, "Transfer from " + self.category)
            return True

        return False

    def check_funds(self, amt):
        balance = self.get_balance()

        if (amt > balance):
            return False

        return True


def create_spend_chart(categories):
    return categories
