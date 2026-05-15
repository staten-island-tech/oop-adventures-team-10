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
        print(f"| Debt to be payed: ${self.debt}")
        print(f"| Balance: ${self.money}")
        print("| Hunger:", self.hunger)
    def activities(self):     
        print("|⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|")
        print("|                     Locations")
        print("| Casino")
        print("| Horse Stables")
        print("| Restaurant")
        print("| Loan Sharks")
        print("| Your House")
        print("|")
        print("|                    Miscellanous")
        print("| Check Wallet")
        print("| Check Pockets")
    def daily(self):
        self.hunger = 100
        self.time = 6
        self.debt -= difficulties[self.x]["daily payment"]