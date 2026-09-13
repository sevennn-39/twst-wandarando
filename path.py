print("There's a forest here...")
print("Welcome to Yonder~!")
print("Warnings: story makes no sense, mild horror, no save system so be really sure about your choices.")
import random
food = 0
sanity = 10
health = 10
gear = 0
blessed = 0
pacifist = 0
fighter = 0
judging = 0
friendship = 0
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
                    fighter += 1
                    if gear > 0: print("You're armed! Special abilities unlocked.")
                if fight1 == "feed it":
                    pacifist += 1
                    print("You toss some of your meat at the spider!")
                    flip1 = random.randint(1,2)
                    if flip1 == 1:
                        print("It takes a bite of the meat, satiated.")
                    if flip1 == 2:
                        print("The spider is not pleased with your sacrifice!")
                        health -= 1
                        print("ATTACK! The spider rends your flesh.")
                if fight1 == "run":
                    print("You try to leave!")
                    pacifist += 1
                    flip2 = random.randint(1,2)
                    if flip2 == 1:
                        print("Success! You run back to the path and continue on.")
                    if flip2 == 2:
                        print("Failure! The spider clicks its jaws menacingly.")
                        health -= 1
                        print("ATTACK! The spider rends your flesh.")
                if fight1 == "try to reason with it":
                    pacifist += 1
                    judging += 1
                    print("You try to talk to the spider - do you even know if it has ears?")
                    talk1 = input("Options: say something smart, say something stupid, yell at it ")
                    if talk1 == "say something smart":
                        print("You decide to impress the spider with your knowledge of fun facts!")
                        flip3 = random.randint(1,2)
                        if flip3 == 1:
                            print("The spider is impressed! It trundles off.")
                        if flip3 == 2:
                            print("The spider finds your fact not fun enough. It screeches.")
                            health -= 1
                            print("ATTACK! The spider rends your flesh.")
    if forest1 == "go right":
        print("You opt for the path on the right!")
        print("It's quiet here...")
        right1 = input("Options: keep going, pause to look around ")
        if right1 == "keep going":
            print("You decide to keep going!")
        if right1 == "pause to look around":
            judging += 1
            print("Your gaze goes from the trees around you to the leaf-strewn path to a cottage in the distance.")
        forest2 = input("Continue on? Options: yes/no ")
        if forest2 == "yes":
            print("As you walk on, you notice the cottage in the distance!")
        if forest2 == "no":
            print("Too bad! You take a minute to pause, then continue on.")
        print("You approach the cottage. It's dark inside.")
        house1 = input("Options: barge in, knock, yell ")
        if house1 == "barge in":
            fighter += 1
            print("You kick the cottage's door open to reveal an empty room!")
            house2 = input("Options: look around the room, start throwing stuff ")
            if house2 == "look around the room":
                print("You walk further into the cottage, noticing the old photos on the walls and half-cleaned dishes in the sink.")
            if house2 == "start throwing stuff": 
                print("You trudge further into the cottage, grab the closest heavy object - a lamp - and throw it against the back wall.")
                print("Nothing happens.")
        if house1 == "yell":
            print("You opt to yell through the door - 'HELLO? IS ANYBODY HOME?', but recieve no answer.")
            house4 = input("Options: open the door, knock ")
            if house4 == "open the door":
                print("You slowly open the door. The cottage is empty and dark.")
                house5 = input("Options: look around the room, start throwing stuff ")
        if house1 == "knock":
            print("You knock politely on the cottage door. Once, then twice. Nothing happens.")
            pacifist += 1
            house3 = input("Options: open the door, ask if anyone's home ")
            if house3 == "open the door":
                print("You slowly open the door. The cottage is empty and dark.")

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
    print("Reload for a new route!")