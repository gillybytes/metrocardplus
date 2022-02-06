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
choice = int(input("""Enter the number of your choice:
1. Add funds.
2. Calculate rides.
"""))
print(choice)