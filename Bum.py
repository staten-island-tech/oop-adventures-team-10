import random
import time
healt = 100
z = 1
class Bum:
    def __init__(self, name, friendliness, anger, greed, days_without_food):
        self.name = name
        self.frnd = friendliness
        self.angr = anger
        self.greed = greed
        self.day = days_without_food
Unamed_bum = Bum('bum', 1, 1, 1, 1)
Unamed_bum.frnd = random.randint(1,100) # Friendliness
Unamed_bum.angr = random.randint(1,100) # Anger
Unamed_bum.day = random.randint(1,10) # Days Without Food
print("___________________HOMELESS_BUM____________________")
print("           ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  ❤️  ❤️                ")
print("days without food: ", Unamed_bum.day)
if Unamed_bum.day >= 8:
    print("Damn he dead")
elif Unamed_bum.day < 8:
    if Unamed_bum.day >= 5 and Unamed_bum.frnd >= 50:
        Unamed_bum.greed = random.randint(50,100)
    elif Unamed_bum.day < 5 and Unamed_bum.frnd >= 50:
        Unamed_bum.greed = random.randint(25,75)
    elif Unamed_bum.day >= 5 and Unamed_bum.frnd < 50:
        Unamed_bum.greed = random.randint(1,50)
    else:
        Unamed_bum.greed = random.randint(25, 75)
    x = input("Do you want to poke him with a stick to check his friendliness?").upper()
    if x != "NO":
        print("Okie")
        print("You poke him with a stick...")
        time.sleep(0.5)
        if Unamed_bum.frnd >= 80:
            print("Bum - WTF man! You got some money fo me?")
        elif Unamed_bum.frnd >= 60:
            print("Bum - Aye, hop off with the stick! Before I give you BTA!!")
        elif Unamed_bum.frnd >= 40:
            print("The bum stands up")
            print("Bum - On your left buddy!")
            print(" - 10 HP")
            healt -= 10
            print("Bum - Maybe next time you will think twice buddy!") 
        elif Unamed_bum.frnd >= 0:
            print("The Bum dashes up!")
            print("INBOUND CRACK ATTACK")
            print("Bum - On ur right buddy!")
            print(" - 20 HP")
            healt -= 20
            print("Bum - Some of the white stuff in yo face!")
            print("*all_purpose_flour.tm* Thrown in your face")
            while z <= 10:
                print("Poison damage! - 5 HP")
                healt -= 5
                time.sleep(0.5)
                x += 1