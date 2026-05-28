import random
import requests

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
        x = 1
    val += int(x)
print(val)

# Do you want to hit or stand?

while val <= 21:
    ht_stnd = input("Hit or Stand: ").upper()

    if ht_stnd == "HIT":
        response = requests.get(url)
        z = (cards["cards"][c]["value"]).upper()
        v = (cards["cards"][c]["suit"]).upper()
        print(z,"of", v)
        if z == "JACK" or z == "KING" or z == "QUEEN":
            z = 10
        elif z == "ACE":
            z = 1
        val += int(z)
        c += 1

    elif ht_stnd == "STAND":
        break

    else:
        print("It's hit or stand buddy")

    print(val)

if val >= 22:
    print("You busted everywhere")

else:
    print("final value:", val)

# Dealers Deck

print("Your dealers deck")
for i in range(2):
    response = requests.get(url)
    x = (cards["cards"][c]["value"]).upper()
    y = (cards["cards"][c]["suit"]).upper()
    print(x,"of", y)
    if x == "JACK" or x == "KING" or x == "QUEEN":
        x = 10
    elif x == "ACE":
        x = 1
    val1 += int(x)
    c += 1
print(val1)

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
        x = 1
    val1 += int(x)
    c += 1