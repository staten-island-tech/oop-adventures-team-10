import time
import json
import random
import py

difficulties = json.load(open("oop-adventures-team-10./difficulties.json", encoding="utf8"))
classdata = py.load(open("oop-adventures-team-10./data.py", encoding="utf8"))

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
        print("\"I'm here to take another loan.\" (This will add to your current debt and interest will be applied accordingly.)")
