import time
import json
import random

difficulties = json.load(open("oop-adventures-team-10./difficulties.json", encoding="utf8"))

class character:
    def __init__(self, name, debt, interest, payments, money, hunger, time):
        self.name = name
        self.debt = debt
        self.interest = interest
        self.payments = payments
        self.money = money
        self.hunger = hunger
        self.time = time
    def terminal(self):
        print("|⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|")
        print("|", self.name)
        print("|", self.time)
        print("| Debt to be payed:", self.debt)
        print("| Balance: $", self.money)
        print("| Hunger:", self.hunger)
    def activities(self):     
        print("|⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|")
        print("|                     Locations")
        print("| Casino")
        print("| Horse Stables")
        print("| Restaurant")
        print("| Your House")
        print("|")
        print("|                    Miscellanous")
        print("| Check Wallet")
        print("| Check Pockets")
    def daily(self):
        self.hunger = 100
        self.time = 6
        self.debt -= difficulties[self.x]["daily payment"]
        self.debt *= difficulties[self.x]["weekly interest"]




difficulties = json.load(open("oop-adventures-team-10./difficulties.json", encoding="utf8"))
currentdiff = int(10)
trueorfalse = 0
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

player = character(input("What is your name? "), difficulties[currentdiff]["starting debt"], difficulties[currentdiff]["weekly interest"], difficulties[currentdiff]["daily payment"], 50000, 100, 6)

while player.money >= 0 and player.hunger >= 0:
    wipescreen(50)
    player.terminal()
    player.activities()
    action = input()