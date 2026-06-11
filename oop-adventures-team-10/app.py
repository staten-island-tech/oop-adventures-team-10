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
player = character("", difficulties[currentdiff]["starting debt"], difficulties[currentdiff]["interest"], 50000, 100, 360, "N/A", 0, 100, [])
player.name = input("What is your name? ")
while len(player.name) > 40:
    player.name = input("Please enter a name less than 40 characters long. ")

while player.money >= 0 and player.hunger >= 0 and player.health > 0:
    wipescreen(50)
    player.terminal()
    player.action = str(input().lower())
    if random.randint(1,2) == 1:
        z = 1
        print("___________________HOMELESS_BUM____________________")
        print("           ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  ❤️                ")
        print("You encounter a bum!")
        bum_frnd = random.randint(1,100) # Friendliness
        chk_bum = input("Do you want to poke him with a stick to check his friendliness? ").upper()
        if chk_bum != "NO":
            print("Okie")
            print("You poke him with a stick...")
            time.sleep(0.5)
            if bum_frnd >= 80:
                print("Bum - WTF ma! You got sum moneh fo me?")
            elif bum_frnd >= 60:
                print("Bum - Ay, hop off with the stick! Before I givve you BTA!!")
            elif bum_frnd >= 40:
                print("The bum stands up")
                print("Bum - On yo lef sheethed!")
                print(" - 10 HP")
                healt -= 10
                print("Bum - Maybb nex time you think twice!") 
            elif bum_frnd >= 10:
                print("The Bum dashes up!")
                time.sleep(0.5)
                print("INBOUND CRACK ATTACK")
                time.sleep(0.5)
                print("Bum - On yo righ bud!")
                time.sleep(0.5)
                print(" - 20 HP")
                healt -= 20
                print("Bum - Some of the white stuff in yo face!")
                time.sleep(0.5)
                print("*all_purpose_flour.tm* Thrown in your face")
                while z <= 10:
                    print("Poison damage! - 5 HP")
                    healt -= 5
                    time.sleep(1)
                    z += 1
            elif bum_frnd >= 0:
                print("THE BUM CASTS FIREBALL!")
                print("-100 HP!")
                healt -= 100
                print("Title Screen")
                print("How you die lmaooo")
            time.sleep(1)
        else:
            print("You choose not to poke the bum.")
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
    else:
        print("Enter a valid course of action.")
    if player.action == "sleep":
        wipescreen(25)
        print("Going to sleep...")
        time.sleep(2)
        player.time = 360
        player.daily()