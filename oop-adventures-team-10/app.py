import time
import json

difficulties = json.load(open("oop-adventures-team-10./difficulties.json", encoding="utf8"))
currentdiff = int(10)

def wipescreen(x):
        print("")

input("You've been slacking. You've racked up millions of debt, and you need to pay it back in full. Otherwise, it'll be quite unfortunate.")
for parts in difficulties:
    print(parts["difficulty"], ": Start with a debt of $", parts["starting debt"])

currentdiff = input("Choose a difficulty: ").lower()
while currentdiff < 0 or currentdiff > 4:
    for parts in difficulties:
        if currentdiff == parts["difficulty"] or currentdiff == parts["number"]:
            currentdiff = parts["number"]
            break
    if currentdiff != 0 and currentdiff != 1 and currentdiff != 2 and currentdiff != 3 and currentdiff != 4:
        currentdiff = 10
        print("Choose a valid difficulty: ")
print("Success")