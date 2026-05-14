import random
import time
race = True
print("Welcome to the el horsey where u lose all ur money, but theres a chance you can make 5 buckaroos!")
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
while race == True:
    h1 = random.randint(1,8)
    time.sleep(random.randint(1, 2))
    h2 = random.randint(1,8)
    time.sleep(random.randint(1, 2))
    h3 = random.randint(1,8)
    while h1 == h2:
        h2 = random.randint(1,8)
    while h3 == h2 or h3 == h1:
        h3 = random.randint(1,8)
    print(h1)
    print(h2)
    print(h3)