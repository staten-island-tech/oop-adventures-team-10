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
player = character(input("What is your name? "), difficulties[currentdiff]["starting debt"], difficulties[currentdiff]["interest"], 50000, 100, 6, "N/A", 0)

while player.money >= 0 and player.hunger >= 0:
    wipescreen(50)
    player.terminal()
    player.activities()
    player.action = str(input().lower())
    wipescreen(25)
    if "loan shark" in player.action:
        player.loansharks()
    if "casino" in player.action:
        time.sleep(2)
        print("Heading to the Casino")
        player.casino()
    player.time += 1
    if player.time == 22 or player.action == "sleep":
        wipescreen(25)
        print("Going to sleep...")
        time.sleep(2)
        player.time = 6
        player.daily()