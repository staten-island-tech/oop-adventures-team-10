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
time.sleep(0.5)
if mode == "top 3 horses":
    horseval3 = int(input("8 Horses! Choose 3! Choose Wisely! Ex: 123: "))
    time.sleep(0.5)
    print("You have inputed horses", horseval3, ", is that correct?")
    accuracy1 = input("").lower()
elif mode == "big winner":
    print("ex: 1")
    horseval1 = int(input("8 Horses! Choose 1! Choose Wisely! Ex: 1: "))
    time.sleep(0.5)
    print("You have inputed horse", horseval1, ", is that correct?")
    accuracy1 = input("").lower()