# This is the entry point of the MetroCardPlus program.
# ASCII art in Varsity by patorjk.com

from Card import Card


print("""
 ____    ____        _                     ______                       __  _______  __                  
|_   \  /   _|      / |_                 .' ___  |                     |  ]|_   __ \[  |                 
  |   \/   |  .---.`| |-'_ .--.   .--.  / .'   \_| ,--.   _ .--.   .--.| |   | |__) || | __   _   .--.   
  | |\  /| | / /__\\\| | [ `/'`\]/ .'`\ \| |       `'_\ : [ `/'`\]/ /'`\\' |   |  ___/ | |[  | | | ( (`\]  
 _| |_\/_| |_| \__.,| |, | |    | \__. |\ `.___.'\// | |, | |    | \__/  |  _| |_    | | | \_/ |, `'.'.  
|_____||_____|'.__.'\__/[___]    '.__.'  `.____ .'\\'-;__/[___]    '.__.;__]|_____|  [___]'.__.'_/[\__) ) 
""")
print("Welcome to MetroCardPlus!")
start_bal = float(input("To begin, enter your MetroCard starting balance: $"))

metrocard = Card(start_bal)
expiry = input("Enter the expiration date in the format YYYY-MM-DD: ")
metrocard.set_expiration(expiry)
print()
print(metrocard, "\n")

print("What would you like to do next?")
choice = int(input("""1. Add funds.
2. Calculate the number of rides.
3. See balance.
4. See expiration date.
Enter the number of your choice: """))
print()

while choice > 4:
    choice = int(input("Please enter a number 1 thru 4, inclusive: "))

if choice == 1:
    amount = float(input("Enter the amount you'd like to add: $"))
    metrocard.add_value(amount)
elif choice == 2:
    print("To do")
elif choice == 3:
    metrocard.get_balance()
else:
    metrocard.get_expiry_date()