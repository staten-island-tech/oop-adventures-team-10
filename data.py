import json
diff = open("./difficulties.json", encoding="utf8")
difficulties = json.load(diff)

class character:
    def __init__(self, debt, money, caloricsurplus, time, x):
        self.debt = debt
        self.money = money
        self.caloricsurplus = caloricsurplus
        self.time = time
        self.x = x
    def terminal():
        print("| {self.time}")
        print("| Debt owed: {self.debt}")
        print("| Balance: ${self.money}")
        print("| Hunger: {caloricsurplus}")
    def daily():
        self.time = 6
        self.debt -= difficulties[self.x]["daily payment"]
        self.debt *= difficulties[self.x]["weekly interest"]