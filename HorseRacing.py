import random
import time
x = 1
race = True
print("Welcome to the el horsey where u lose all ur money, but theres a chance you can make 5 buckaroos!")
time.sleep(1)
accuracy = "no"
accuracy1 = "no"
accuracy2 = "no"
while accuracy == "no":
    betval = float(input("How much would you like to bet today? "))
    time.sleep(0.5)
    print("You have inputed", betval, "dollars, is that correct?")
    accuracy = input("").lower()
mode = input("'top 3 horses' or 'big winner' ").lower()
time.sleep(0.5)
if mode == "top 3" or mode == "top 3 horses":
    while accuracy1 == "no":
        horseval3_1 = int(input("8 Horses! Choose 3! Choose Wisely! Choose your first horse here! "))
        horseval3_2 = int(input("8 Horses! Choose 3! Choose Wisely! Choose your second horse here! "))
        horseval3_3 = int(input("8 Horses! Choose 3! Choose Wisely! Choose your third horse here! "))
        time.sleep(0.5)
        print("You have inputed horses", horseval3_1, horseval3_2, "and", horseval3_3, ", Correct?")
        accuracy1 = input("").lower()
elif mode == "big winner":
    while accuracy2 == "no":
        horseval1 = int(input("8 Horses! Choose 1! Choose Wisely! Ex: 1: "))
        time.sleep(0.5)
        print("You have inputed horse", horseval1, ", is that correct?")
        accuracy2 = input("").lower()
print("Let's begin the race!!!")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GO!!!")
time.sleep(1)
while race == True:
    h1 = random.randint(1,8)
    h2 = random.randint(1,8)
    h3 = random.randint(1,8)
    while h1 == h2:
        h2 = random.randint(1,8)
    while h3 == h2 or h3 == h1:
        h3 = random.randint(1,8)
    print("_______________Lap", x,"________________")
    print("Top 3 horses: ")
    print("|Lead Horse:", h1)
    print("|Second Place:", h2)
    print("|Third Place:", h3)
    time.sleep(2)
    x += 1
    if x >= 4:
        print("Final Winners!", h1, h2, h3)
        break
if mode == "top 3" or mode == "top 3 horses":
    time.sleep(1)
    if horseval3_1 == h1 and horseval3_2 == h2 and horseval3_3 == h3:
        print("Congratulations!!!!")
        print("Your three chosen horses have won!!!")
        print("Your inputed cash has been multiplied by 50!!!")
        betval *= 50
        print(betval)
    else:
        print("Stinky Run today, huh")
        betval -= betval
        print("Final Outcome,", betval, "dollars")
elif mode == "big winner":
    time.sleep(1)
    if horseval1 == h1:
        print("Congrats!!!!")
        print("Your chosen lead horse has won!!!")
        print("Your inputed cash has been multiplied by 5!!!")
        betval *= 5
        print(betval)
    else:
        print("Stinky Run today, huh")
        betval -= betval
        print("Final Outcome,", betval, "dollars")