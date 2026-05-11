import random
import time
print("Welcome to the amazing world of Horse Racing!")
time.sleep(1)
accuracy = "no"
while accuracy == "no":
    betval = input("How much would you like to bet today? ")
    time.sleep(0.5)
    print("You have inputed", betval, "dollars, is that correct?")
    accuracy = input("").lower()
mode = input("'top 3 horses' or 'big winner' ").lower()
time.sleep(1)
if mode == "top 3 horses":
    horseval3 = int(input("8 Horses! Choose 3! Choose Wisely! Ex: 1 2 3"))
elif mode == "big winner":
    print("ex: 1")
    horseval1 = int(input("8 Horses! Choose 3! Choose Wisely! Ex: 1"))