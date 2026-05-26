import random
import requests

# BlackJack
val = 0
x2 = 0
name = "m"

def getCards():
    url = "https://deckofcardsapi.com/api/deck/new/draw/?count=4"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
cards = getCards()

print("The dealer has dealed you your cards...")
for i in range(2):
    url = "https://deckofcardsapi.com/api/deck/new/draw/?count=4"
    response = requests.get(url)
    x = (cards["cards"][i]["value"]).upper()
    y = (cards["cards"][i]["suit"]).upper()
    print(x,"of", y)
    if x == "JACK" or x == "KING" or x == "QUEEN":
        x = 10
    elif x == "ACE":
        x = 1
    else:
        val += int(x)

print(val)