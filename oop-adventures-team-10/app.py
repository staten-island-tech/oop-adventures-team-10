import time
import json
import random
from data import character

difficulties = json.load(open("oop-adventures-team-10./difficulties.json", encoding="utf8"))
currentdiff = int(10)
trueorfalse = 0
def wipescreen(x):
    for i in range(x):
        print("")

wipescreen(50)
input("You've been slacking. You've racked up millions of dollars in debt, and you need to pay it back in full. Otherwise, it'll be quite unfortunate.")
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
player = character(input("What is your name? "), difficulties[currentdiff]["starting debt"], difficulties[currentdiff]["interest"], 50000, 100, 360, "N/A", 0, 100)

while player.money >= 0 and player.hunger >= 0 and player.health > 0:
    wipescreen(50)
    player.terminal()
    player.action = str(input().lower())
    wipescreen(25)
    if "loan shark" in player.action:
        player.loansharks()
    elif "casino" in player.action:
        print("Heading to the Casino...")
        time.sleep(1)
        wipescreen(35)
        print("Welcome to the casino!")
        player.casino()
    else:
        print("Enter a valid course of action.")
    if player.action == "sleep":
        wipescreen(25)
        print("Going to sleep...")
        time.sleep(2)
        player.time = 360
        player.daily()