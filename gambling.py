import random
import requests

# BlackJack

#Hearts (\(\hearts \)): A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
#Diamonds (\(\diamonds \)): A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
#Clubs (\(\clubs \)): A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
#Spades (\(\spades \)): A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K

name = "m"
url = "https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

print("Good afternoon", name, "welcome to blackjack...")

