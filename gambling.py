import random
import requests
import time
# BlackJack
val = 0
val1 = 0
name = "m"
c = 3
# Geting Cards

def getCards():
    url = "https://deckofcardsapi.com/api/deck/new/draw/?count=21"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
cards = getCards()

# Your Cards

print("_________________________Your cards________________________")

print("The dealer has dealed you your cards...")
for i in range(2):
    url = "https://deckofcardsapi.com/api/deck/new/draw/?count=21"
    response = requests.get(url)
    x = (cards["cards"][i]["value"]).upper()
    y = (cards["cards"][i]["suit"]).upper()
    print(x,"of", y)

    if x == "JACK" or x == "KING" or x == "QUEEN":
        x = 10

    elif x == "ACE":
        if val <= 11:
            x = 10
        elif val >= 12:
            x = 1
    val += int(x)
print("🔵 your value", val)

# Do you want to hit or stand?

while val <= 21:
    ht_stnd = input("Hit or Stand: ").upper()

    if ht_stnd == "HIT":
        response = requests.get(url)
        x = (cards["cards"][c]["value"]).upper()
        y = (cards["cards"][c]["suit"]).upper()
        print(x,"of", y)
        if x == "JACK" or x == "KING" or x == "QUEEN":
            x = 10
        elif x == "ACE":
            if val <= 11:
                x = 10
            elif val >= 12:
                x = 1
        val += int(x)
        c += 1
        print("🔵 your value", val)
        time.sleep(0.5)
    elif ht_stnd == "STAND":
        break

    else:
        print("It's hit or stand buddy")

print("🔵 your final value", val)

# Your Outcome

if val >= 22:
    print("You busted everywhere")

# Dealers Deck

print("______________________Dealer's cards______________________")

if val <= 21:
    print("Your dealers deck")
    for i in range(2):
        response = requests.get(url)
        x = (cards["cards"][c]["value"]).upper()
        y = (cards["cards"][c]["suit"]).upper()
        print(x,"of", y)
        if x == "JACK" or x == "KING" or x == "QUEEN":
            x = 10
        elif x == "ACE":
            if val1 <= 11:
                x = 10
            elif val1 >= 12:
                x = 1
        val1 += int(x)
        c += 1
    print("🔴 dealers value", val1)
    time.sleep(0.5)
    # Dealer Hits or Stands

    while val1 <= 16:
        print("Dealer Hits")
        response = requests.get(url)
        x = (cards["cards"][c]["value"]).upper()
        y = (cards["cards"][c]["suit"]).upper()
        print(x,"of", y)

        if x == "JACK" or x == "KING" or x == "QUEEN":
            x = 10

        elif x == "ACE":
            if val1 <= 11:
                x = 10
            elif val1 >= 12:
                x = 1
        val1 += int(x)
        c += 1
        print("🔴 dealers value", val1)
        time.sleep(0.5)
    print("🔴 dealers final value", val1)

    # Dealer Outcome

    if val1 >= 22:
        print("Dealer busted everywhere")

    # Game outcome

    if val1 <= 21:
        if val > val1:
            print("You Won!!")
        elif val == val1:
            print("It's a tie!")
        else:
            print("You lostt")

else:
    print("You lostt")


