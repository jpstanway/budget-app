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


def create_category_strings(categories):
    global catNames

    for index, cat in categories:
        name = [char for char in cat.category]

        if (index == 0):
            catNames = name

        print('next name', name)
        for idx, letter in enumerate(name):
            print('next idx', idx)
            if catNames[idx]:
                catNames[idx] += letter
            else:
                catNames[idx] = ''

    return catNames


def create_spend_chart(categories):
    heading = "Percentage spent by category\n"
    chart = ""
    space = " "
    percentage = 100
    dividerLen = (3 * len(categories)) + 1
    divider = (space * 4) + ("-" * dividerLen)
    cats = create_category_strings(categories)
    print('cats', cats)

    while percentage >= 0:
        percent = str(percentage)
        chart += space * (3 - len(percent))
        chart += percent + "|\n"
        percentage -= 10

    return heading + chart + divider
