import time
import json
import random

from data import character

difficulties = json.load(open("oop-adventures-team-10./difficulties.json", encoding="utf8"))


currentdiff = int(10)
trueorfalse = 0
action = "I"
def wipescreen(x):
    for i in range(x):
        print("")

input("You've been slacking. You've racked up millions of debt, and you need to pay it back in full. Otherwise, it'll be quite unfortunate.")
wipescreen(100)
for parts in difficulties:
    print(parts["difficulty"], ": Start with a debt of $", parts["starting debt"])
currentdiff = input("Choose a difficulty: ").lower()
while trueorfalse != True:
    for parts in difficulties:
        if currentdiff == parts["difficulty"].lower() or currentdiff == parts["number"]:
            currentdiff = parts["number"]
            trueorfalse = 1
            break
    if trueorfalse != True:
        currentdiff = input("Choose a valid difficulty: ").lower()
player = character(input("What is your name"), difficulties[currentdiff]["starting debt"], difficulties[currentdiff]["weekly interest"], difficulties[currentdiff]["daily payment"], 50000, 100, 6)

while player.money >= 0 and player.hunger >= 0:
    wipescreen(50)
    player.terminal()
    player.activities()
    action = input().lower()
    wipescreen(25)
    if "loan shark" in action:
        print("You head to the loan sharks to pay off your debt.")
        wipescreen(5)
        print(f"Loan Shark guy: \"Let's see, you're {player.name}. What are you here for?\"")
        wipescreen(5)
        print("Your Options:")
        print("1.\"I'm here to take another loan.\" (This will add to your current debt and interest will be applied accordingly.)")
        print("2.\"I'm here to pay back some of my debt.\"(Minimum of $5,000 accepted.)")
        print("3.\"Actually, nevermind. I'll be heading out.\"")
        if input == "1":
            print("Loan Shark guy: \"Well how much are you looking to borrow?\"")
            action = input()
            while action < 100 or action > 10000000:
                if action < 100:
                    print("Loan Shark guy: \"What? You came here just to borrow that little? Borrow some money or get the **** out.\"")
                elif action > 10000000:
                    print("\"I know your *** ain't gonna be able to pay all that, either get serious or get out.\"")
                action = input()
            print("\"All right, you're good to go. Now get going.\"")
            player.debt += action