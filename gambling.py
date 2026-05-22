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
while x2 <= 1:
    url = "https://deckofcardsapi.com/api/deck/new/draw/?count=4"
    response = requests.get(url)
    x = (cards["cards"][x2]["value"]).upper()
    y = (cards["cards"][x2]["suit"]).upper()
    x2 += 1
    print(x,"of", y)
if x == "JACK" or x == "KING" or x == "QUEEN":
    val += 10
    print(val)