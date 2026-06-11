import time
import random
import requests
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
def getCards():
    url = "https://deckofcardsapi.com/api/deck/new/draw/?count=54"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
class Deck:
    def __init__(self):
        self.cards = []
        self.fetch_deck()
    def fetch_deck(self):
        url = "https://deckofcardsapi.com/api/deck/new/draw/?count=52"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                self.cards = response.json()["cards"]
        except Exception as e:
            print(f"Error connecting to API: {e}")
    def getcard(self):
        if self.cards:
            return self.cards.pop(0)
        return None
class blackjackplayer:
    def __init__(self, name, hand, total):
        self.name = name
        self.hand = hand
        self.total = total
    def recievecard(self, card):
        self.hand.append(card)
    def scorecalc(self):
        self.total = 0
        value = 0
        aces = 0
        for card in self.hand:
            value = card["value"].upper()
            if value in ["JACK", "QUEEN", "KING"]:
                self.total += 10
            elif value == "ACE":
                self.total += 11
                aces += 1
            else:
                self.total += int(value)
        while self.total > 21 and aces > 0:
            self.total -= 10
            aces -= 1
        return value
    def show_hand(self):
        self.scorecalc()
        print(f"\n--- {self.name} Hand ---")
        for card in self.hand:
            print(f"{card['value']} of {card['suit']}")
        print(f"Total Value: {self.total}")
def wipescreen(x):
    for i in range(x):
        print("")

class horseandjockey:
    def __init__(self, horsename, jockeyname, horsespeed, jockeyskill, distancerun):
        self.horsename = horsename
        self.jockeyname = jockeyname
        self.horsespeed = horsespeed
        self.jockeyskill = jockeyskill
        self.distancerun = distancerun
    def race(self):
        if self.distancerun < 2000:
            self.distancerun += round(random.randint(5, 10) + ((self.horsespeed/100) * (self.jockeyskill/100) * 10), 2)
            self.distancerun = round(self.distancerun, 2)
        if self.distancerun >= 2000:
            self.distancerun = 2000
            if self.jockeyname not in finishingrankings:
                finishingrankings.append(self.jockeyname.title())
    def raceprint(self):
        print(f"{f'{'|':⣿<{self.distancerun/10}}':<200}|⡪|  {self.jockeyname}, {self.distancerun} meters")
diego = horseandjockey("Silver Bullet", "Diego Brando", 90, 98, 0)
johnny = horseandjockey("Slow Dancer", "Johnny Joestar", 95, 85, 0)
gyro = horseandjockey("Valkyrie", "Gyro Zeppeli", 90, 93, 0)
pocoloco = horseandjockey("Hey! Ya!", "Pocoloco", 85, 95, 0)
tim = horseandjockey("Ghost Rider in the Sky", "Mountain Tim", 96, 90, 0)
hotpants = horseandjockey("Gets Up", "Hot Pants", 89, 95, 0)
sandman = horseandjockey("None (He'll be on foot)", "Sandman", 97, 93, 0)
racers = [diego, johnny, gyro, pocoloco, tim, hotpants, sandman]
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
        print("| Job Center                                                                                         |")
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
            while True:
                try:
                    self.action = float(0)
                    while self.action <= 0:
                        self.action = float(input("Enter a value:"))
                    break
                except ValueError:
                    print("Enter a valid number.")        
            print("\"All right, you're good to go. Now get going.\"")
            self.debt += self.action
            self.money += self.action
            self.time += 15
    def casino(self):
        print("|⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺ ⎺|")
        print("|                   Town Casino                     |")
        print("|                                                   |")
        print("|                                                   |")
        print("|                /⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺\                   |")
        print("|                |Blackjack Table|                  |")
        print("|                \______________/                   |")
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
        elif self.action == "blackjack":
            self.blackjacktable()
        elif self.action == "exit":
            print("Leaving the casino...")
            time.sleep(1)
    def blackjacktable(self):
        while True:
            try:
                self.bet = float(input("How much would you like to bet? "))
                if self.bet <= 0:
                    print("You have to bet a positive amount of money. ")
                elif self.bet > self.money:
                    print("You cannot bet more money than you have. ")
                else:
                    break
            except ValueError:
                print("Please enter a valid number")
        time.sleep(0.5)
        print("Very well, good luck")
        deck = Deck()
        you = blackjackplayer(f"{self.name}'s", [], 0)
        dealer = blackjackplayer("Dealer's", [], 0)
        for i in range(2):
            you.recievecard(deck.getcard())
            dealer.recievecard(deck.getcard())
        you.show_hand()
        dealer.show_hand()
        self.casino()
        while you.total < 21:
            action = input("\nHit or Stand? ").lower()
            if action == "hit":
                you.recievecard(deck.getcard())
                you.show_hand()
            elif action == "stand":
                break
            else:
                print("Please type 'hit' or 'stand'.")
        if you.total <= 21:
            dealer.show_hand()
            while dealer.total < 17:
                print("\nDealer hits...")
                time.sleep(1)
                dealer.recievecard(deck.getcard())
                dealer.show_hand()
        if you.total > 21:
            print(f"Dang man, that's rough, better luck next time.")
        elif dealer.total > 21:
            print(f"Dealer busted. You win ${self.bet * 2}!")
        elif you.total > dealer.total:
            print(f"Congrats!, your money has been doubled! +${self.bet * 2}")
        elif you.total < dealer.total:
            print(f"Dang man, that's rough, better luck next time.")
        else:
            print(f"It's a push.")
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
        input("")
        self.casino()
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
        for racer in racers:
            racer.distancerun = 0
        places = 0
        selections = []
        multi = 0
        self.action = "no"
        mode = "N/A"
        race = True
        global finishingrankings
        x = 0
        self.bet = float(0)
        finishingrankings = []
        print("Welcome to the el horsey where u lose all ur money, but theres a chance you can make 5 buckaroos!")
        print("")
        print("Racers:")
        for i in racers:
            print(f"{f'Jockey: {i.jockeyname}':<25} Horse: {i.horsename}")
        print("")
        print(f"Your balance: ${self.money}")
        while True:
            try:
                while float(self.bet) <= 0:
                    self.bet = float(input("How much are you betting? $"))
                break
            except ValueError:
                print("Invalid input.")
        self.bet = round(self.bet, 2)
        self.money -= self.bet
        while "trifecta" != mode and "single winner" != mode:
            mode = input("Bet on a trifecta or single winner. ").lower()
        time.sleep(0.5)
        self.action == "no"
        finishingrankings = []
        if "trifecta" == mode:
            for i in range(3):
                self.action = ""
                while x == 0:
                    self.action = input(f"Choose your racer for {i+1}. ").lower()
                    for index, racer in enumerate(racers):
                        if self.action not in selections and self.action == str(racer.jockeyname).lower():
                            x = 1
                selections.append(self.action.title())
                print(f"You've selected: {selections}")
                x = 0
        elif "single winner" in mode:
            self.action = ""
            while x == 0:
                self.action = input("Select your racer: ").lower()
                for racer in racers:
                    if self.action == racer.jockeyname.lower():
                        selections.append(racer.jockeyname.title())
                        x = 1
            x = 0
        print("Let's begin the race!!!")
        for i in range(3):
            time.sleep(1)
            print(3-i)
        print("GO!!!")
        time.sleep(1)
        while race == True: #actual race happens
            wipescreen(10)
            for i in racers:
                i.race()
                i.raceprint()
            race = False
            for index, racer in enumerate(racers):
                if racer.distancerun < 2000:
                    race = True
            time.sleep(0.2)
        print("And the race is over!")
        input("")
        print("Race rankings:")
        for index, racer in enumerate(finishingrankings):
            print(f"{index+1}. {racer}")
        print("Your ranking(s)")
        for index, racer in enumerate(selections):
            print(f"{index+1}. {racer}")
        if "trifecta" in mode:
            x = True
            for index, racer in enumerate(selections):
                if str(racer) != finishingrankings[index]:
                    x = False
            if x == True:
                multi = random.randint(50, 80)
                print("Congrats on the win!")
                print(f"You've won ${self.bet * multi} at a {multi}x multiplier.")
                self.money += self.bet * multi
            else:
                print("Stinky Run today, huh?")
                print("Final Outcome, $0.") 
        elif mode == "single winner":
            if selections[0] == finishingrankings[0]:
                multi = random.randint(80, 100)/10
                self.bet = round((self.bet * multi), 2)
                print("Congrats!!!!")
                print("Your chosen lead horse has won!!!")
                print(f"You've won ${self.bet} at a {multi}x multiplier!")
                self.money += self.bet
            else:
                print("Stinky Run today, huh")
                print("Final Outcome, $0.")
        self.time += 75
        input("")
    def work(self):
        print("You look for a job everwhere, but nobody is willing to hire you.")
        input("")