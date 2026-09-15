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
                spiderhealth = 10
                if food > 0: print("You've got meat! Special option unlocked: feed it.")
                fight1 = input("Options: fight, try to reason with it ")
                if fight1 == "fight":
                    print("You opted to fight!")
                    fighter += 1
                    if gear > 0: print("You're armed! Special protection unlocked.")
                    print("You toss a nearby stick at the spider with all your strength.")
                    health -= 1
                    spiderhealth -= 1
                    print("The spider is aggravated. ATTACK! The spider rends your flesh.")
                if fight1 == "feed it":
                    pacifist += 1
                    print("You toss some of your meat at the spider!")
                    flip1 = random.randint(1,2)
                    if flip1 == 1:
                        print("It takes a bite of the meat, satiated. For now.")
                        spiderhealth += 1
                    if flip1 == 2:
                        print("The spider is not pleased with your sacrifice!")
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
                            print("The spider is impressed! It trundles off. For now.")
                        if flip3 == 2:
                            print("The spider finds your fact not fun enough. It screeches.")
                            health -= 1
                            print("ATTACK! The spider rends your flesh.")
                fight2 = input("Next action! Options: fight, try to reason with it ")
                if health == 9: 
                    print("Remember, you're injured! Use caution! Your current health: 9/10")
                if fight2 == "fight":
                    fighter += 1
                    print("You grab a stick and toss it at the spider. Interesting.")
                    flip5 = random.randint(1,2)
                    if flip5 == 1:
                        spiderhealth -= 1
                        print("Your attack hits!")
                    if flip5 == 2:
                        print("Your throw goes wide!")
                        print("The spider is displeased. ATTACK! The spider grabs you in its mandibles.")
                        health -= 1
                    
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
        if house1 == "yell":
            judging += 1
            print("You opt to yell through the door - 'HELLO? IS ANYBODY HOME?', but recieve no answer.")
            house4 = input("Options: open the door, knock ")
            if house4 == "open the door":
                print("You slowly open the door.")
        if house1 == "knock":
            print("You knock politely on the cottage door. Once, then twice. Nothing happens.")
            pacifist += 1
            house3 = input("Options: open the door, ask if anyone's home ")
        if house1 == "open the door":
            print("You slowly open the door.")
        print("You enter the cottage but see only an empty room!")
        house2 = input("Options: look around the room, start throwing stuff ")
        if house2 == "look around the room":
            print("You walk further into the cottage, noticing the old photos on the walls and half-cleaned dishes in the sink.")
        if house2 == "start throwing stuff": 
            print("You trudge further into the cottage, grab the closest heavy object - a lamp - and throw it against the back wall. A photo shatters on the floor.")
            print("Nothing happens.")
        house4 = input("Options: investigate the photos, throw more stuff ")
        if house4 == "investigate the photos":
            print("You walk towards the back wall of the cottage, looking at the framed photos.")
            print("They're all of a family: a mother, a grandmother, and their son/grandson. They smile happily together.")
            print("The photo is faded.")
            print("What happened to them?")
            think1 = input("Options: think about the photos more, investigate more of the cottage. ")
            if think1 == "think about the photos more":
                print("You devote some of your attention to the photos again. A kid and a family...")
                print("Where did they go? Why did they go?")
                print("There are still dishes in the sink. It's not normal.")
                print("You turn your attention to the rest of the cottage.")
            if think1 == "investigate more of the cottage":
                print("There have to be clues elsewhere, right?")
            print("You look around the rest of the cottage. There are two rooms off the main one, dirty dishes in the sink, and a vase of wilted flowers on the table.")
            house5 = input("Options: look at the left room, look at the right room, look at the dishes, look at the flowers ")
            if house5 == "look at the left room":
                print("You walk through the threshold to the room on the left. It's a bedroom - draped with cozy knitted patterns, shades of burgundy and gold.")
                print("It's homey. Or to be more accurate - it reminds you of home.")
                print("You walk towards the other room to go check.")
                print("The room on the right is ")
            if house5 == "look at the right room":
                print("You enter the threshold of the room on the right. It's another bedroom - this one in blue and white, clouds painted on the ceiling and walls. There's a rainbow in the corner.")
                print("This is a kids' room. It's sad to see all of the hand-carved wooden toys gathering dust.")

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