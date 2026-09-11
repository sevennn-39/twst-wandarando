print("There's a forest here...")
print("Welcome to Yonder~!")
import random
food = 0
sanity = 10
health = 10
gear = 0
blessed = 0
pacifist = 0
fighter = 0
judging = 0
weird = random.randint(1,10)
in1 = input("Options: Stay put, go investigate, go into town (make sure to write exactly) ")
if in1 == "stay put":
    print("You don't do anything! Kind of boring, isn't it?")
    print("Reload for a new route!")
if in1 == "go investigate":
    print("You enter the forest! It's kinda creepy here...")
    forest1 = input("Options: go left, go right, go straight ")
    if forest1 == "go left":
        print("You opt for the left path! Oooh, spooky...")
        left1 = input("Options: continue on, stop to observe ")
        if left1 == "continue on":
            print("You head down the path.")
            print("There's a disturbance in the brush!")
            left2 = input("Options: look at it, ignore it ")
            if left2 == "look at it":
                print("You approach the disturbance...")
                print("It's a giant spider. Fight triggered!")
                if food > 0: print("You've got meat! Special option unlocked: feed it.")
                fight1 = input("Options: fight, run, try to reason with it ")
                if fight1 == "fight":
                    print("You opted to fight!")
                    if gear > 0: print("You're armed! Special abilities unlocked.")
                if fight1 == "feed it":
                    print("You toss some of your meat at the spider!")
if in1 == "go into town":
    print("You decide to go into town for supplies!")
    in3 = input("Options: go to the butchers, go to the armory, or go to the chapel ")
    if in3 == "go to the butchers":
        print("You've opted for a restock of meat!")
        meat = input("Get some food? yes/no ")
        if meat == "yes":
            food += 1
            print("You have acquired some food!")
    if in3 == "go to the armory":
        print("Time to get suited up!")
        armor = input("Get some armor? yes/no ")
        if armor == "yes":
            gear += 1
            print ("You have acquired one set of armor!")
    if in3 == "go to the chapel":
        print("You've chosen to go to the chapel!")
        blessing = input("Pray? yes/no ")
        if blessing == "yes":
            blessed += 1
    print("Your duties are done!")
    reset = input("Back to the beginning? yes/no ")
