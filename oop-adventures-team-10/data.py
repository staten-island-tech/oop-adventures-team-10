import time
import random
food = [
    {
        "Food": "8in Pepperoni Pizza",
        "Price": 29.99,
        "Hunger filled": 10
    },
    {
        "Food": "Cheeseburger",
        "Price": 14.99,
        "Hunger filled": 5
    },
    {
        "Food": "Fifty gram tin of Caviar",
        "Price": 499.99,
        "Hunger filled": 2
    },
    {
        "Food": "Plate of Spaghetti and Meatballs",
        "Price": 39.99,
        "Hunger filled": 12
    },
    {
        "Food": "Steak and Potatoes",
        "Price": 99.99,
        "Hunger filled": 20
    },
    {
        "Food": ,
        "Price": ,
        "Hunger filled":
    },
    {
        "Food": ,
        "Price": ,
        "Hunger filled":
    },
]

class character:
    def __init__(self, name, debt, interest, money, hunger, time, action, bet, health):
        self.name = name
        self.debt = debt
        self.interest = interest
        self.money = money
        self.hunger = hunger
        self.time = time
        self.action = action
        self.bet = bet
        self.health = health
    def terminal(self):
        print("|⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|")
        print(f"{f'| {self.name}':<101}|")
        print(f"{f'| Time {self.time // 60}:{self.time % 60:02}':<101}|")
        print(f"{f'| Debt to be payed: ${self.debt}':<101}|")
        print(f"{f'| Balance: ${self.money}':<101}|")
        print(f"{f'| Hunger: {self.hunger}':<101}|")
        print("|⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|")
        print("|                     Locations                                                                      |")
        print("| Casino                                                                                             |")
        print("| Horse Stables                                                                                      |")
        print("| Restaurant                                                                                         |")
        print("| Loan Sharks                                                                                        |")
        print("| Local McDonalds                                                                                    |")
        print("| Your House                                                                                         |")
        print("|                                                                                                    |")
        print("|                    Miscellanous                                                                    |")
        print("| Check Wallet                                                                                       |")
        print("| Check Pockets                                                                                      |")
        print("⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺")
    def daily(self):
        self.hunger -= 20
        self.time = 360
        self.debt = round(self.debt*self.interest, 2)
    def loansharks(self):
        print("You head to the loan sharks to pay off your debt.")
        print(f"Loan Shark guy: \"Let's see, you're {self.name}. What are you here for?\"")
        print("Your Options:")
        print("1.\"I'm here to take another loan.\" (This will add to your current debt and interest will be applied accordingly.)")
        print("2.\"I'm here to pay back some of my debt.\"(Minimum of $5,000 accepted.)")
        print("3.\"Actually, nevermind. I'll be heading out.\"")
        self.action = input("")
        if self.action == "1":
            print("Loan Shark guy: \"Well how much are you looking to borrow?\"")
            self.action = float(input(""))
            while self.action < 100 or self.action > 10000000:
                if self.action < 100:
                    print("Loan Shark guy: \"What? You came here just to borrow that little? Borrow some money or get the **** out.\"")
                elif self.action > 10000000:
                    print("\"I know your *** ain't gonna be able to pay all that, either get serious or get out.\"")
                self.action = input()
            print("\"All right, you're good to go. Now get going.\"")
            self.debt += self.action
            self.money += self.action
    def casino(self):
        print("|⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺|")
        print("|                   Town Casino                     |")
        print("|                                                   |")
        print("|                                                   |")
        print("|   /⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺\       /⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺\           |")
        print("|   |Blackjack Table|       |Poker Table|           |")
        print("|   \_______________/       \___________/           |")
        print("|                                                   |")
        print("|                                                   |")
        print("|     ________________        _________             |")
        print("|    |Russian Roulette|      |Coin Flip|            |")
        print("|     ⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺        ⎺⎺⎺⎺⎺⎺⎺⎺⎺             |")
        print("|                                                   |")
        print("|                     V Exit V                      |")
        print("|___________________________________________________|")
        print("")
        self.action = input("Where would you like to go?").lower()
        if self.action == "russian roulette":
            print("Well hello there kid, care for a game of Russian Roulette? You will be betting everything, yes?")
            if input("").lower() == "yes":
                print("Well, I'll go first.")
                time.sleep(1.5)
                print("He spins the barrel.")
                time.sleep(1.5)
                for i in range(5):
                    if i == 0 or i == 2 or i == 4:
                        print("The man puts the gun up to his head and you hear a click...")
                        time.sleep(1)
                        if random.randint(0, 5-i) == 0:
                            input("Bang! The revolver goes off and you win.")
                            self.money *= 2
                            break
                        else:
                            print("He survives. He hands the gun to you.")
                            time.sleep(1)
                    else:
                        print("You put the gun up to your head and you hear a click...")
                        time.sleep(1)
                        if random.randint(0, 5-i) == 0:
                            input("Bang! The revolver goes off and you're dead.")
                            self.health = -123456789
                            break
                        else:
                            print("You're safe. You hand the shady man the revolver.")
                            time.sleep(1)
                self.time += 15
                self.hunger -= 5
            else:
                print("Ha, well too bad.")
                time.sleep(2)
                for i in range(25):
                    print("")
                self.casino()
        elif self.action == "coin flip":
            print("In this game, you flip a coin and if it lands on the face you call you double your bet. What's your bet?  ")
            self.bet = round(float(input(" ")), 2)
            while self.bet > self.money:
                self.bet = round(float(input("You cannot wager more than you have, enter a valid amount.  ")), 2)
            print(f"Wagered ${self.bet}.")
            print("Flipping coin...")
            time.sleep(1)
            while self.action != "heads" and self.action != "tails":
                self.action = input("Heads or tails?  ").lower()
            if "heads" == self.action:
                if random.randint(0,1) == 1:
                    print("Tails! You lose!")
                    self.money -= self.bet
                else:
                    print("Heads! You win!")
                    self.money += self.bet
            elif "tails" == self.action:
                if random.randint(0,1) == 1:
                    print("Tails! You win!")
                    self.money += self.bet
                else:
                    print("Heads! You lose!")
                    self.money -= self.bet
            input("")
            self.time += 10
            self.hunger -= 5
            for i in range(25):
                print("")
            self.casino()
        elif self.action == "exit":
            print("Leaving the casino...")
            time.sleep(1)
    def restaurant(self):
        print("Waiter: Welcome, let me get you a seat and here's your menu.")
        print("")
        print("|⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|")
        print("|                                                                                                    |")
        print("|                                                                                                    |")
        print("|                                                                                                    |")
        print("|                                                                                                    |")
        print("|                                                                                                    |")
        print("|                                                                                                    |")
        print("|                                                                                                    |")
        print("⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺")
    def work(self):
        print("In development")