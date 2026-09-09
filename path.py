print("There's a forest here...")
print("Welcome to Yonder~!")
import random
food = 0
sanity = 10
health = 10
gear = 0
blessed = 0
weird = random.randint(1,10)
in1 = input("Options: Stay put, go investigate, go into town (make sure to write exactly)")
if in1 == "stay put":
    print("You don't do anything! Kind of boring, isn't it?")
    print("Reload for a new route!")
if in1 == "go investigate":
    print("You enter the forest! It's kinda creepy here...")
    forest1 = input("Options: go left, go right, go straight")
if in1 == "go into town":
    print("You decide to go into town for supplies!")
    in3 = input("Options: go to the butchers, go to the armory, or go to the chapel")
    if in3 == "go to the butchers":
        print("You've opted for a restock of meat!")
        meat = input("Get some food? yes/no")
        if meat == "yes":
            food += 1
            print("You have acquired some food!")
    if in3 == "go to the armory":
        print("Time to get suited up!")
        armor = input("Get some armor? yes/no")
        if armor == "yes":
            armor += 1
            print ("You have acquired one set of armor!")
    if in3 == "go to the chapel":
        print("You've chosen to go to the chapel!")
        blessing = input("Pray? yes/no")
        if blessing == "yes":
            blessed += 1
    print("Your duties are done!")
    reset = input()
