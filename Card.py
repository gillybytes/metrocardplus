from datetime import date

class Card:
    FARE = 2.75
    balance = 0.0
    expiration = None

    def __init__(self, bal):
        self.balance = bal
        self.expiration = date.today()

    def __repr__(self):
        return "Your MetroCard has a balance of ${bal} and expires on {expiry}.".format(bal=self.balance, expiry=self.expiration)

    def get_balance(self):
        print("Balance: ${0}".format(self.balance))

    def get_expiry_date(self):
        print("Expiration Date: {0}".format(self.expiration))

    def set_expiration(self, expiry):
        self.expiration = expiry

    def add_value(self, amount):
        self.balance += amount

# Test Card class
metrocard = Card(20)
date_str = '2023-02-06'
metrocard.set_expiration(date.fromisoformat(date_str))
print(metrocard)
metrocard.add_value(2.75)
metrocard.get_balance()