import time
import json
import random
from data import character

difficulties = json.load(open("oop-adventures-team-10/difficulties.json", encoding="utf8"))
currentdiff = int(10)
trueorfalse = 0
def wipescreen(x):
    for i in range(x):
        print("")


wipescreen(50)
input("You've been slacking. You've racked up millions of dollars in debt, and you need to pay it back in full. Otherwise, it'll be quite unfortunate. [Enter to continue] ")
wipescreen(100)
for parts in difficulties:
    print(f"{parts["difficulty"].title()}: Start with a debt of ${parts["starting debt"]}")
currentdiff = input("Choose a difficulty: ").lower()
while trueorfalse != True:
    for parts in difficulties:
        if currentdiff == parts["difficulty"] or currentdiff == int(parts["number"]+1):
            currentdiff = parts["number"]
            trueorfalse = 1
            break
    if trueorfalse != True:
        currentdiff = input("Choose a valid difficulty: ").lower()
player = character("", difficulties[currentdiff]["starting debt"], difficulties[currentdiff]["interest"], 50000, 100, 360, "N/A", 0, 100, [])
player.name = input("What is your name? ")
while len(player.name) > 40:
    player.name = input("Please enter a name less than 40 characters long. ")

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
    elif "restaurant" in player.action:
        print("Walking to the restaurant...")
        time.sleep(1)
        wipescreen(30)
        player.restaurant()
    elif "check wallet" in player.action:
        player.checkwallet()
    elif "horse race" in player.action:
        print("Going to the horse races...")
        time.sleep(1)
        player.horseracing()
    elif "job" in player.action:
        print("Going to the job center...")
        time.sleep(1)
        player.work
    else:
        print("Enter a valid course of action.")
    if player.action == "sleep":
        wipescreen(25)
        print("Going to sleep...")
        time.sleep(2)
        player.time = 360
        player.daily()