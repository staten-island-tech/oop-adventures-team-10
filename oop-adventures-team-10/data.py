import time
import random
food = [
    {
        "food": "8in Pepperoni Pizza",
        "price": 29.99,
        "hunger filled": 10
    },
    {
        "food": "Cheeseburger",
        "price": 14.99,
        "hunger filled": 5
    },
    {
        "food": "Fifty gram tin of Caviar",
        "price": 499.99,
        "hunger filled": 2
    },
    {
        "food": "Plate of Spaghetti and Meatballs",
        "price": 39.99,
        "hunger filled": 12
    },
    {
        "food": "Steak and Potatoes",
        "price": 99.99,
        "hunger filled": 20
    },
    {
        "food": "Barbeque Pork Ribs",
        "price": 59.99,
        "hunger filled": 15
    }
]


class character:
    def __init__(self, name, debt, interest, money, hunger, time, action, bet, health, wallet):
        self.name = name
        self.debt = debt
        self.interest = interest
        self.money = money
        self.hunger = hunger
        self.time = time
        self.action = action
        self.bet = bet
        self.health = health
        self.wallet = wallet
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
        print("| Horse Races                                                                                        |")
        print("| Restaurant                                                                                         |")
        print("| Loan Sharks                                                                                        |")
        print("| Local McDonalds                                                                                    |")
        print("| Your House                                                                                         |")
        print("|                                                                                                    |")
        print("|                    Miscellanous                                                                    |")
        print("| Check Wallet                                                                                       |")
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
        print("|   /⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺\     /⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺\          |")
        print("|   |Blackjack Table|     |Roulette Wheel|          |")
        print("|   \_______________/     \_____________/           |")
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
        for data in food:
            print("|⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|")
            print(f"{f'| {data["food"]} ${data["price"]}, Hunger value: {data["hunger filled"]}':<101}|")
        print("⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺")
        print("7 to exit. 1 through 6 to order.")
        self.action = int(input(""))
        while self.action != 7:
            if self.action < 7 and self.action > 0:
                if self.money > food[self.action-1]["price"]:
                    self.money -= food[self.action-1]["price"]
                    self.hunger += food[self.action-1]["hunger filled"]
                    print(f"Ordered {food[self.action-1]["food"]}")
                    self.money = round(self.money, 2)
                    if self.hunger > 125:
                        self.hunger = 125
                    self.action = int(input(""))
            else:
                self.action = int(input("Choose a valid course of action."))
    def checkwallet(self):
        print("Wallet")
        print("|⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|")
        print("| |⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺|                  |")
        print("| |       New Mexico                  Identification Card             |                  |")
        print(f"{f'| | ⠀⠀⠀⠀⠀⠀⢀⣴⣾⡿⢿⣿⣷⣤⠀⠀ ⠀⠀⠀    2   {self.name}':<70}|                  |")
        print("| | ⠀⠀⠀⠀⠀⠀⡿⠁⠀⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀    3    DOB: 9/7/1958                        |                  |")
        print("| | ⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠸⣿⡆⠀⠀⠀⠀    8    308 Negra Arroyo Lane                |                  |")
        print("| | ⠀⠀⠀⠀⠀⢸⣷⣀⠀⠀⠀⠀⣀⣸⣿⣇⠀⠀⠀⠀         Albuquerque, NM 87104                |                  |")
        print("| | ⠀⠀⠀⠀⠀⢺⣿⠿⠿⢻⡇⣿⠛⢿⢿⡟⠀⠀⠀⠀    15   SEX: M                               |                  |")
        print("| | ⠀⠀⠀⠀⠀⠘⣿⡒⠐⣺⡇⢻⣗⢲⣿⠃⠀⠀⠀⠀    18   EYES: BRO                            |                  |")
        print("| | ⠀⠀⠀⠀⠀⠀⢸⣷⣴⣾⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀    16   HGT: 5'-11\"                          |                  |")
        print("| | ⠀⠀⠀⠀⠀⢀⣼⣿⣿⡍⢿⣿⣿⣿⣇⠀⠀⠀⠀⠀                                              |                  |")
        print("| | ⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀                                              |                  |")
        print("| | ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿                                              |                  |")
        print("| |_⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿______________________________________________|                  |")
        print(f"{f'| {self.wallet}':<91}|")
        input("|________________________________________________________________________________________|")
    def horseracing(self):
        multi = 0
        self.action = "no"
        accuracy1 = "no"
        accuracy2 = "no"
        x = 1
        mode = "N/A"
        race = True
        print("Welcome to the el horsey where u lose all ur money, but theres a chance you can make 5 buckaroos!")
        time.sleep(1)
        while self.action == "no":
            self.bet = float(input("How much would you like to bet today? "))
            time.sleep(0.5)
            print(f"Your bet is ${self.bet}, correct?")
            self.action = input("").lower()
        while not "trifecta" in mode and not "single winner" in mode:
            mode = input("Bet on a trifecta or single winner. ").lower()
        time.sleep(0.5)
        self.action == "no"
        if "trifecta" in mode:
            while self.action == "no":
                horseval3_1 = int(input("8 Horses! Choose 3! Choose Wisely! Choose your first horse here! "))
                horseval3_2 = int(input("8 Horses! Choose 3! Choose Wisely! Choose your second horse here! "))
                horseval3_3 = int(input("8 Horses! Choose 3! Choose Wisely! Choose your third horse here! "))
                time.sleep(0.5)
                print("You have inputed horses", horseval3_1, horseval3_2, "and", horseval3_3, ", correct?")
                self.action = input("").lower()
        elif "single winner" in mode:
            while self.action == "no":
                horseval1 = int(input("8 Horses! Choose 1! Choose Wisely! Ex: 1: "))
                time.sleep(0.5)
                print("You have inputed horse", horseval1, ", is that correct?")
                self.action = input("").lower()
        self.money -= self.bet
        print(self.money)
        print("Let's begin the race!!!")
        for i in range(3):
            time.sleep(1)
            print(3-i)
        print("GO!!!")
        time.sleep(1)
        while race == True:
            h1 = random.randint(1,8)
            h2 = random.randint(1,8)
            h3 = random.randint(1,8)
            while h1 == h2:
                h2 = random.randint(1,8)
            while h3 == h2 or h3 == h1:
                h3 = random.randint(1,8)
            print("_______________Lap", x,"________________")
            print("Top 3 horses: ")
            print("|Lead Horse:", h1)
            print("|Second Place:", h2)
            print("|Third Place:", h3)
            time.sleep(2)
            x += 1
            if x >= 4:
                print("Final Winners!", h1, h2, h3)
                break
        if "trifecta" in mode:
            time.sleep(1)
            if horseval3_1 == h1 and horseval3_2 == h2 and horseval3_3 == h3:
                multi = random.randint(3500, 5500)/10
                print("Congratulations!!!!")
                print("Your three chosen horses have won!!!")
                self.bet = round((self.bet * multi), 2)
                print(f"Congratulations, you've won ${self.bet}!")
                self.money += self.bet
            else:
                print("Stinky Run today, huh?")
                print("Final Outcome, 0 dollars")
        elif mode == "single winner":
            time.sleep(1)
            if horseval1 == h1:
                multi = random.randint(80, 100)/10
                self.bet = round((self.bet * multi), 2)
                print("Congrats!!!!")
                print("Your chosen lead horse has won!!!")
                print(f"You've won {self.bet}")
                self.money += self.bet
            else:
                print("Stinky Run today, huh")
                print("Final Outcome, $0.")
    def work(self):
        print("In development")

