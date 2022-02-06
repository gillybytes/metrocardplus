from datetime import date

class Card:
    FARE = 2.75

    def __init__(self, bal):
        self.balance = bal
        self.rides = self.calc_rides()
        self.expiration = date.today()

    def __repr__(self):
        return "Your MetroCard has a balance of ${bal}, which equals {rides} rides, and expires on {expiry}.".format(bal=self.balance, rides=self.rides, expiry=self.expiration)

    def get_balance(self):
        print("Balance: ${0}".format(self.balance))

    def get_expiry_date(self):
        print("Expiration Date: {0}".format(self.expiration))

    def get_rides(self):
        print("Rides Remaining: {0}".format(self.rides))

    def set_expiration(self, expiry):
        self.expiration = expiry

    def add_value(self, amount):
        self.balance += amount
        self.rides = self.calc_rides()
        print("${0} has been added.".format(amount))

    def update_balance(self, num):
        self.calc_rides(num)
        self.balance = self.rides * self.FARE

    def calc_rides(self, taken=0):
        if taken > 0:
            self.rides -= taken
        else:
            self.rides = int(self.balance / self.FARE)
        return self.rides


# Test Card class
# metrocard = Card(8.75)
# date_str = '2023-02-06'
# metrocard.set_expiration(date.fromisoformat(date_str))
# print(metrocard)
# metrocard.add_value(2.75)
# metrocard.get_rides()