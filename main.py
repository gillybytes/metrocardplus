# This is the entry point of the MetroCardPlus program.
# ASCII art in Varsity by patorjk.com

from Card import Card

logo = """
 ____    ____        _                     ______                       __  _______  __                  
|_   \  /   _|      / |_                 .' ___  |                     |  ]|_   __ \[  |                 
  |   \/   |  .---.`| |-'_ .--.   .--.  / .'   \_| ,--.   _ .--.   .--.| |   | |__) || | __   _   .--.   
  | |\  /| | / /__\\\| | [ `/'`\]/ .'`\ \| |       `'_\ : [ `/'`\]/ /'`\\' |   |  ___/ | |[  | | | ( (`\]  
 _| |_\/_| |_| \__.,| |, | |    | \__. |\ `.___.'\// | |, | |    | \__/  |  _| |_    | | | \_/ |, `'.'.  
|_____||_____|'.__.'\__/[___]    '.__.'  `.____ .'\\'-;__/[___]    '.__.;__]|_____|  [___]'.__.'_/[\__) ) 
"""

menu = """What would you like to do next?
1. Add funds.
2. Calculate remaining rides.
3. See balance.
4. See expiration date.
5. Exit program.
"""

def get_user_input():
    return int(input(menu + "Enter the number of your choice: "))


print(logo)
print("Welcome to MetroCardPlus!")
start = float(input("To begin, enter your MetroCard balance: $"))

metrocard = Card(start)
expiry = input("Enter the expiration date in the format YYYY-MM-DD: ")
metrocard.set_expiration(expiry)
print()
print(metrocard, "\n")

choice = get_user_input()
print()

while choice != 5:
    while choice < 1 or choice > 5:
        choice = int(input("Please enter a number 1 thru 5, inclusive: "))
    if choice == 1:
        amount = float(input("Enter the amount you'd like to add: $"))
        metrocard.add_value(amount)
        metrocard.get_balance()
        print()
        choice = get_user_input()
    elif choice == 2:
        print(metrocard.calc_rides(), "\n")
        choice = choice = get_user_input()
    elif choice == 3:
        metrocard.get_balance()
        print()
        choice = get_user_input()
    elif choice == 4:
        metrocard.get_expiry_date()
        print()
        choice = get_user_input()
