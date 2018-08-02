import diceRolling
import playerChar

def userInput(user_input):
    return user_input.lower().split(" ")

def main():
    print("You are about to embark on an epic adventure, full of magic, fighting and intrigue.")
    print()
    print("First, however, you have to shake a hangover, figure out how to be a person again")
    print("and determine your path to said adventure.")
    print()
    print("It begins in darkness.")
    print()
    print("-------------------------------------------------------------------------------------------")
    print()

    print("You open your eyes. You're lying on the ground.")
    print("You plumb the depths of what memories you have left for your name, you find it.")

    name = input("What is your name? If you don't answer, it'll be set to a default name which is pretty stupid so you may as well put something down... ")

    player = playerChar.newPC()

    if name != "":
        player.change_name(name)

    print(player.char_name)
    
    control_signal_1 = 0
    control_signal_2 = 0
    control_signal_3 = 0
    control_signal_4 = 0
    control_signal_5 = 0
    
    counter = 0
    loop_control = 0

    while loop_control == 0:

        user_input = userInput(input("What do you want to do?"))

        
        
        if user_input[0] == "look":
            if len(user_input) == 1:
                print("Look where? Try saying 'look left' or 'look right'")
            else:
                if user_input[1] == "left":
                    print("You see darkness...")
                    counter += 1
                    if counter == 3:
                        print("Huh, it's almost like there's darkness in ALL directions, weird... but definitely keep trying")
                    elif counter == 5:
                        print("SERIOUSLY, MAYBE TRY SOMETHING ELSE, 'HELP' MIGHT BE UP YOUR ALLEY")
                    
                elif user_input[1] == "right":
                    print("You see darkness...")
                    counter += 1
                    if counter == 3:
                        print("Huh, it's almost like there's darkness in ALL directions, weird... but definitely keep trying")
                    elif counter == 5:
                        print("SERIOUSLY, MAYBE TRY SOMETHING ELSE, 'HELP' MIGHT BE UP YOUR ALLEY")
                    
                elif user_input[1] == "up":
                    print("You see darkness...")
                    counter += 1
                    if counter == 3:
                        print("Huh, it's almost like there's darkness in ALL directions, weird... but definitely keep trying")
                    elif counter == 5:
                        print("SERIOUSLY, MAYBE TRY SOMETHING ELSE, 'HELP' MIGHT BE UP YOUR ALLEY")
                    
                elif user_input[1] == "down":
                    print("You see darkness...")
                    counter += 1
                    if counter == 3:
                        print("Huh, it's almost like there's darkness in ALL directions, weird... but definitely keep trying")
                    elif counter == 5:
                        print("SERIOUSLY, MAYBE TRY SOMETHING ELSE, 'HELP' MIGHT BE UP YOUR ALLEY")
                    
                else:
                    print("Huh, you said 'look {0}' which either doesn't make sense or isn't a viable command, try again".format(user_input[1]))

        elif user_input[0] == "search":
            if len(user_input) == 1:
                print("Search where, bud?")
            else:
                if user_input[1] == "ground" or user_input[2] == "ground":
                    print("You grope around on the ground and your hands stumble across a large rock, it could be used as an impromptu weapon...")
                    control_signal_1 = 1

                elif user_input[1] == "pockets" or user_input[2] == "pockets" or user_input[1] == "pocket" or user_input[2] == "pocket" or user_input[1] == "self" or user_input[1] == "myself":
                    print("You search in all your pockets and luckily find a box of tinder and a flint. You don't remember putting it there, but then again, you don't remember anything pretty much.")
                    print("Classic amnesia...")
                    control_signal_2 = 1

                elif user_input[1] == "memories" or user_input[2] == "memories" or user_input[1] == "memory" or user_input[2] == "memory":
                    print("You don't remember anything other than the clink of glasses and the dull roar of a crowded tavern. That explains the pounding headache and the nausea. That's no good.")

                else:
                    print("Search where now?? You said 'search {0}' but that really doesn't make sense or maybe we didn't program that response, try something else, hoss.".format(user_input[1]))

        elif user_input[0] == "take":
            if len(user_input) == 1:
                print("Take what...? Try again, this time with an object in mind")
            else:
                if (user_input[1] == "tinder" or (user_input[1] + user_input[2]) == "tinderbox" or user_input[1] == "tinderbox" or user_input[1] == "box" or user_input[1] == "flint") \
                    and control_signal_2 == 1:
                    print("You take the tinder box and flint, you little pyro, you")
                    control_signal_2 = 0
                    player.inventory.append("tinder box and flint")

                elif (user_input[1] == "rock" or user_input[2] == "rock") and control_signal_1 == 1:
                    print("You grab the rock, heft it, good weight to it. You stick it in your backpack in case you need it later.")
                    control_signal_1 = 0
                    player.inventory.append("rock")

                elif (user_input[1] + user_input[2] + user_input[3] + user_input[4]) == "stockofthesituation":
                    print("Well it isn't great...you've woken up in god only knows where, splitting headache and what's the weird noise you're hearing...")

        elif user_input[0] == "shout" or user_input[0] == "yell" or user_input[0] == "scream":
            print("You shout into the darkness, your voice echoes back at you from the dark.")

        
                    
        
        elif user_input[0] == "stand" or (user_input[0] + user_input[1]) == "getup":
            print("You are currently standing up, congratulations on figuring out basic motor control, pssshhh, just fyi, babies do that every day. Baby.")
            control_signal_3 = 1 #the control signal that allows the player to fight further on in level 1

        if "tinder box and flint" in player.inventory:
            
            if user_input[0] == "light" or user_input[0] == "set":
                if len(user_input) == 1:
                    print("errr, bud, do what now... '{0} what?'".format(user_input))

                else:
                    if user_input[1] == "fire":
                        print("Hey, presto, you light a fire...")
                        loop_control = 1

    print()
    print("Wow, you've stood up and made a fire, this must be a big day for you!")
    print("however... at the edge of the light, you notice a GIANT RAT chittering and looking menacing")
    print("slowly it moves closer to you, clearly looking to eat...")
    print()

    user_input = userInput(input("What do you want to do?"))

                           
    

    loop_control = 0

    while loop_control == 0:

        
        if user_input[0] == "stand" or (user_input[0] + user_input[1]) == "getup":
            if control_signal_3 == 1:
                print("bruh, you're already standing, you can't stand twice that just doesn't even make sense.")
            else:
                print("You are currently standing up, congratulations on figuring out basic motor control, pssshhh, just fyi, babies do that every day. Baby.")

        elif user_input[0] == "search":
            if len(user_input) == 1:
                print("Search where, bud?")
            else:
                if user_input[1] == "ground" or user_input[2] == "ground":
                    if control_signal_1 == 1:
                        print("Really...you already searched here...")
                    else:
                        print("You grope around on the ground and your hands stumble across a large rock, it could be used as an impromptu weapon.")

                elif user_input[1] == "pockets" or user_input[2] == "pockets" or user_input[1] == "pocket" or user_input[2] == "pocket" or user_input[1] == "self" or user_input[1] == "myself":
                    control_signal_2 = 0
                    print("Really...you already searched here...")

                elif user_input[1] == "memories" or user_input[2] == "memories" or user_input[1] == "memory" or user_input[2] == "memory":
                    print("You don't remember anything other than the clink of glasses and the dull roar of a crowded tavern. That explains the pounding headache and the nausea. That's no good.")

                else:
                    print("Search where now?? You said 'search {0}' but that really doesn't make sense or maybe we didn't program that response, try something else, hoss.".format(user_input[1]))

        elif user_input[0] == "fight":
            print("fight what?")
            print("a) giant rat")
            print("b) your demons")
            user_input_2 = userInput(input("Who do you want to fight?"))

            if user_input2[0] == "a" or user_input2[0] == "giant":
                print("You attack the giant rat!")
                temp = diceRolling.roll_d20()
                
                           
                                     
        
    


main()
























                    
