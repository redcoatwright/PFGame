#Things to add:
#1) inventory functionality (ability to select and equip item or use item i.e. rock in this case)
#2) add ability to modify inventory not in combat
#3) add look descriptions after lighting fire when the PC can see stuff (mostly just caves and whatnot)
#4) inventory choice should be wrapped in try/catch block not loop over keys of dict

import utilities.diceRolling
import utilities.playerChar
import utilities.natMonsters
import combat
import time
import utilities.weaponList

dice = utilities.diceRolling
player_mod = utilities.playerChar
monsters = utilities.natMonsters
weapons = utilities.weaponList

def userInput(user_input):
    return user_input.lower().split(" ")

def main():

    start_time = time.time()

    print(" ____       _   _      __ _           _           ")
    print("|  _ \ __ _| |_| |__  / _(_)_ __   __| | ___ _ __ ")
    print("| |_) / _` | __| '_ \| |_| | '_ \ / _` |/ _ \ '__|")
    print("|  __/ (_| | |_| | | |  _| | | | | (_| |  __/ |   ")
    print("|_|   \__,_|\__|_| |_|_| |_|_| |_|\__,_|\___|_|   ")

    print()
    print("You are about to embark on an epic adventure, full of magic, fighting and intrigue. \n")
    print("First, however, you have to shake a hangover, figure out how to be a person again")
    print("and determine your path to said adventure. \n")
    print()
    print("It begins in darkness...")

    print("            _")
    print(" _         | |")
    print("| | _______| |---------------------------------------------\ ")
    print("|:-)_______|==[]============================================>")
    print("|_|        | |---------------------------------------------/")
    print("           |_|")

    print()

    print("You open your eyes. You're lying on the ground. \n")
    print("You plumb the depths of what memories you have left for your name, you find it. \n")

    name = input("What is your name? If you don't answer, it'll be set to a default name which is pretty stupid so you may as well put something down...  \n \nEnter your name: ")
    print("\n")
    
    player = player_mod.newPC()

    if name != "":
        player.change_name(name)

    print("Hi " + player.char_name + ".\n")

    control_signal_1 = 0
    control_signal_2 = 0
    control_signal_3 = 0
    control_signal_4 = 0
    control_signal_5 = 0
    
    counter = 0
    loop_control = 0

    while loop_control == 0:

        print("What do you want to do?")
        
        user_input = userInput(input("\n >>> "))

        print()
        
        #[x.lower() for x in user_input] #list comprehension to put all items to lowercase

        if len(user_input) == 1:
            
            if user_input[0] == "look":
                print("Look where? Try saying 'look left' or 'look right' \n")

            elif user_input[0] == "search":
                print("Search where, bud? \n")

            elif user_input[0] == "take":
                print("Take what...? Try again, this time with an object in mind. \n")

            elif user_input[0] == "stand":
                print("You are currently standing up, congratulations on figuring out basic motor control, pssshhh, just fyi, babies do that every day. Baby. \n")
                control_signal_3 = 1 #the control signal that allows the player to fight further on in level 1'

            elif user_input[0] == "shout" and user_input[0] == "yell" and user_input[0] == "scream":
                print("You shout into the darkness, your voice echoes back at you from the dark. \n")

            elif user_input[0] == "help":
                print("Here are some commands you can use 'Look (left)', 'Search (the ground)' or look/search other places. \n")

            elif (user_input[0] == "light" or user_input[0] == "set") and control_signal_3 == 1:
                print("errr, bud, do what now... '{0} what?' Try again \n".format(user_input))

            else:
                print("What the hell! You didn't say anything that makes sense! Try again, dummy. \n")

        elif len(user_input) == 2:

            if user_input[0] == "look":
                if user_input[1] == "left":
                    print("You see darkness... \n")
                    counter += 1
                    if counter == 3:
                        print("Huh, it's almost like there's darkness in ALL directions, weird... but definitely keep trying \n")
                    elif counter == 5:
                        print("SERIOUSLY, MAYBE TRY SOMETHING ELSE, 'HELP' MIGHT BE UP YOUR ALLEY \n")
                    
                elif user_input[1] == "right":
                    print("You see darkness... \n")
                    counter += 1
                    if counter == 3:
                        print("Huh, it's almost like there's darkness in ALL directions, weird... but definitely keep trying \n")
                    elif counter == 5:
                        print("SERIOUSLY, MAYBE TRY SOMETHING ELSE, 'HELP' MIGHT BE UP YOUR ALLEY \n")
                    
                elif user_input[1] == "up":
                    print("You see darkness... \n")
                    counter += 1
                    if counter == 3:
                        print("Huh, it's almost like there's darkness in ALL directions, weird... but definitely keep trying \n")
                    elif counter == 5:
                        print("SERIOUSLY, MAYBE TRY SOMETHING ELSE, 'HELP' MIGHT BE UP YOUR ALLEY \n")
                    
                elif user_input[1] == "down":
                    print("You see darkness... \n")
                    counter += 1
                    if counter == 3:
                        print("Huh, it's almost like there's darkness in ALL directions, weird... but definitely keep trying \n")
                    elif counter == 5:
                        print("SERIOUSLY, MAYBE TRY SOMETHING ELSE, 'HELP' MIGHT BE UP YOUR ALLEY \n")
                    
                else:
                    print("Huh, you said 'look {0}' which either doesn't make sense or isn't a viable command, try again \n".format(user_input[1]))

            elif user_input[0] == "search":

                if user_input[1] == "ground":

                    print("You grope around on the ground and your hands stumble across a large rock, it could be used as an impromptu weapon... \n")
                    control_signal_1 = 1

                elif user_input[1] == "pockets" or user_input[1] == "pocket" or user_input[1] == "self" or user_input[1] == "myself":

                    print("You search in all your pockets and luckily find a box of tinder and a flint. You don't remember putting it there, but then again, you don't remember anything pretty much.")
                    print("Classic amnesia... \n")
                    control_signal_2 = 1

                elif user_input[1] == "memories" or user_input[1] == "memory":

                    print("You don't remember anything other than the clink of glasses and the dull roar of a crowded tavern. That explains the pounding headache and the nausea. That's no good. \n")

                else:
                    print("Huh, you said 'search {0}' which either doesn't make sense or isn't a viable command, try again. \n".format(user_input[1]))

            elif user_input[0] == "take":

                if (user_input[1] == "tinder" or user_input[1] == "tinderbox" or user_input[1] == "box" or user_input[1] == "flint") and control_signal_2 == 1:

                    print("You take the tinder box and flint, you little pyro, you. \n")
                    control_signal_2 = 0
                    player.inventory.append("tinder box and flint")

                elif user_input[1] == "rock" and control_signal_1 == 1:

                    print("You grab the rock, heft it, good weight to it. You stick it in your backpack in case you need it later. \n")
                    control_signal_1 = 0
                    player.einventory.append(weapons.Rock())


            elif (user_input[0] + user_input[1]) == "getup" or (user_input[0] + user_input[1]) == "standup":

                print("You are currently standing up, congratulations on figuring out basic motor control, pssshhh, just fyi, babies do that every day. Baby. \n")
                control_signal_3 = 1 #one of the control signals that moves the game state forward'

            elif (user_input[0] + user_input[1]) == "laydown" and control_signal_3 == 1:
                print("You are now laying down again...on the cold dirty floor. Is this where you want to be? \n")
                control_signal_3 = 1
                
            elif (user_input[0] + user_input[1]) == "laydown":

                loop_control_2 = 0

                while loop_control_2 == 0:
                    dumdum = input("Dum dum say what? \n >>> ")
                    
                    if dumdum == "what" or dumdum == "what?":
                        print("Good boy! \nDum dum already laying down... \n")
                        loop_control_2 = 1
                    else:
                        print("Dum dum wrong answer... \n")
                    
            elif ((user_input[0] + user_input[1]) == "lightfire" or (user_input[0] + user_input[1] == "setfire")) and control_signal_3 == 1:
                print("Hey, presto, you light a fire...\n")
                print("It only took you {0} minutes. Thats only 63% slower than the average, congrats!\n".format((time.time() - start_time)/60))
                control_signal_4 = 1
            
            else:
                print("What the hell! You didn't say anything that makes sense! Try again, dummy. \n")
        
        elif len(user_input) == 3:

            if user_input[0] == "search":

                if user_input[2] == "ground":

                    print("You grope around on the ground and your hands stumble across a large rock, it could be used as an impromptu weapon... \n")
                    control_signal_1 = 1

                elif user_input[2] == "pockets" or user_input[2] == "pocket":

                    print("You search in all your pockets and luckily find a box of tinder and a flint. You don't remember putting it there, but then again, you don't remember anything pretty much.")
                    print("Classic amnesia... \n")
                    control_signal_2 = 1

                elif user_input[2] == "memories" or user_input[2] == "memory":

                    print("You don't remember anything other than the clink of glasses and the dull roar of a crowded tavern. That explains the pounding headache and the nausea. That's no good. \n")

                else:
                    
                    print("Search where now?? I didn't understand what you said \n")

            elif user_input[0] == "take":

                if (user_input[1] + user_input[2]) == "tinderbox" and control_signal_2 == 1:

                    print("You take the tinder box and flint, you little pyro, you. \n")
                    control_signal_2 = 0
                    player.inventory.append("tinder box and flint")

                elif user_input[2] == "rock" and control_signal_1 == 1:

                    print("You grab the rock, heft it, good weight to it. You stick it in your backpack in case you need it later. \n")
                    control_signal_1 = 0
                    player.einventory.append(weapons.Rock())

                else:
                    print("Take what now? I don't understand what you said \n")

            elif (user_input[0] + user_input[1] + user_input[2]) == "lightafire" and control_signal_3 == 1:
                print("Hey, presto, you light a fire...\n")
                print("It only took you {0} minutes. Thats only 63% slower than the average, not too shabby!\n".format((time.time() - start_time)/60))
                control_signal_4 = 1

            else:
                print("What the hell! You didn't say anything that makes sense! Try again, dummy. \n")
                
        elif len(user_input) == 5:

            if user_input[0] == "take":
                
                if (user_input[1] + user_input[2] + user_input[3] + user_input[4]) == "stockofthesituation":

                    print("Well it isn't great...you've woken up in god only knows where, splitting headache and what's the weird noise you're hearing... \n")


        else:

            print("What the hell! You didn't say anything that makes sense! Try again111, dummy. \n")
        
        if control_signal_3 == 1 and control_signal_4 == 1:
            loop_control = 1



    print()
    print("Wow, you've stood up and made a fire, this must be a big day for you!")
    print("however... at the edge of the light, you notice a GIANT RAT chittering and looking menacing")
    print("slowly it moves closer to you, clearly looking to eat...")
    print()

    

                           
    

    loop_control = 0

    while loop_control == 0:

        user_input = userInput(input("What do you want to do? \n \n >>> "))

        if len(user_input) == 1:

            if user_input[0] == "search":
                print("Search where, bud?")

            elif user_input[0] == "stand":
                if control_signal_3 == 1:
                    print("bruh, you're already standing, you can't stand twice that just doesn't even make sense.")
                else:
                    print("You are currently standing up, congratulations on figuring out basic motor control, pssshhh, just fyi, babies do that every day. Baby.")

            elif user_input[0] == "fight":

                print("You have entered combat!")
                
                print("fight what?\n")
                print("a) giant rat\n")
                user_input_2 = userInput(input("b) your demons \n \n >>> "))

                if user_input_2[0] == "a" or user_input_2[0] == "giant" or user_input_2[0] == "rat":

                    rat = monsters.Rat()

                    print("You have entered combat with the giant rat!\n")

                    print("These are your current stats vs. the rat's:")

                    print("_____________________________________")
                    print("|     Yours     |vs.|     Rat's     |")
                    print("'''''''''''''''''''''''''''''''''''''")
                    
                    print(" AC: {0}         vs.      AC: {1}    ".format(player.ac,rat.ac))
                    print(" HP: {0}/{1}     vs.      HP: {2}/{3}    ".format(player.c_hp,player.t_hp,rat.c_hp,rat.t_hp))
                    print(" Init: {0}       vs.      Init: {1}  ".format(player.init, rat.init))
                    print(" Atk: {0}        vs.      Atk: {1}   ".format(player.melee_attk, rat.melee_attk))

                    print("'''''''''''''''''''''''''''''''''''''")

                    print("Rolling D20 + init to figure out who goes first!\n")
                    rat_init = dice.roll_d20() + rat.init
                    print("Rat init: {0}\n".format(rat_init))

                    pc_init = dice.roll_d20() + player.init
                    print("Your init: {0}\n".format(pc_init))
                       
                    result = combat.larger_num(rat_init,pc_init)

                    if result == 1:
                            print("\n Looks like the rat goes first! Get ready for some shiiiiiit. \n")
                            control_signal_5 = 2
                            
                    elif result == 0:
                            print("\n You got lucky punk, your move! \n")
                            control_signal_5 = 1

                    else:
                        print("\n Huh, seems you and the rat are equally as motivated to get this thing going.")
                        print("How to deal with this situation! Crazy times, I guess we can just coin toss it. \n")
                        coin = input("Do you want heads or tails? \n >>> ")
                        print("\n 1 is heads, 2 is tails! \n")
                        coin_flip = dice.roll_d2()
                        
                        if (coin == "heads" and coin_flip == 1) or (coin == "tails" and coin_flip == 2):
                            print("\n You got lucky punk, your move! \n")
                            control_signal_5 = 1
                        else:
                            print("\n Looks like the rat goes first! Get ready for some shiiiiiit. \n")
                            control_signal_5 = 2
                    

                    

                    loop_control_2 = 0 

                    while loop_control_2 == 0:

                        
                        
                        
                        print("These are your current stats vs. the rat's:")

                        print("_____________________________________")
                        print("|     Yours     |vs.|     Rat's     |")
                        print("'''''''''''''''''''''''''''''''''''''")
                        
                        print(" AC: {0}         vs.      AC: {1}    ".format(player.ac,rat.ac))
                        print(" HP: {0}/{1}         vs.      HP: {2}/{3}    ".format(player.c_hp,player.t_hp,rat.c_hp,rat.t_hp))
                        print(" Init: {0}       vs.      Init: {1}  ".format(player.init, rat.init))
                        print(" Atk: {0}        vs.      Atk: {1}   ".format(player.melee_attk, rat.melee_attk))

                        print("'''''''''''''''''''''''''''''''''''''")

                        
                        
                        if control_signal_5 == 2:

                            control_signal_5 = 1
                            
                            print("The rat lunges at you, fangs bared...it makes a bite attack!")
                            time.sleep(2)
                            print("Rolling for the rat's attack: \n")
                            atk_res = combat.melee_attack(rat.melee_attk)
                            print("\n The attack is a {0} against your AC of {1} \n".format(atk_res, player.ac))

                            time.sleep(2)
                            
                            if atk_res >= player.ac:
                                print("The attack lands! Oh no, you got bit by the ickle mouse, let's see the damage! \n")
                                dmg_res = combat.dmg(rat.dmg_die,0)
                                print("\n Looks like you were hit for {0} points of hp. \n".format(dmg_res))
                                player.sub_hp(dmg_res)
                                print("Now you're at {0}/{1} \n".format(player.c_hp,player.t_hp))

                            else:
                                print("The attack missed you entirely! What a stupid rat! \n")

                            print("---------------------------------------------------------------------------")
                            
                            
                        elif control_signal_5 == 1:

                            control_signal_5 = 2

                            print("Action Menu:")
                            print("a) Attack")
                            print("b) Run")
                            print("c) Inventory")
                            print("d) Spells\n")
                        
                            user_input_3 = input("What would you like to do? \n >>> ").lower()
                            
                            
                            if user_input_3 not in ["a","b","c","d"]:
                                print("You didn't choose 'a', 'b', 'c' or 'd'! Try again.")

                            else:

                                if user_input_3 == "a":
                                    print("\nAttack!\n")

                                    print(player.equItem.desc)

                                    print("Rolling a d20 for your attack: \n")
                                    atk_res = combat.melee_attack(player.melee_attk)
                                    print("\n The attack is a {0} against the rat's AC of {1} \n".format(atk_res, rat.ac))
                                    
                                    if atk_res >= rat.ac:
                                        print(player.equItem.hit)
                                        print("You successfully punch the mostly harmless mouse, you big jerk. \n")
                                        dmg_res = combat.dmg(player.equItem.die,0)
                                        print("\n Looks like you hit for {0} points of hp. \n".format(dmg_res))
                                        rat.sub_hp(dmg_res)
                                        print("Now the rat is at {0}/{1} \n".format(rat.c_hp,rat.t_hp))

                                        

                                    else:
                                        print(player.equItem.miss)

                                elif user_input_3 == "b":
                                    print("Well this is awkward, you can't run from this fight...you're still learning and all \n")

                                elif user_input_3 == "c":

                                    if player.einventory is []:
                                        print("You have nothing! N-O-T-H-I-N-G \nThere was a rock on the ground you missed, though, just saying... \n")
                                    
                                    else:
                                        print("Here's what is in your inventory: \n")
                                        counter = 1
                                        tdict = dict()
                                        for x in player.einventory:
                                            print("hello: {0}".format(x))
                                            tdict[counter] = x
                                            counter += 1

                                        print(tdict)

                                        loop_control_3 = 0

                                        while loop_control_3 == 0:
                                        
                                            user_input_3 = userInput(input("Select an item by number or enter 'quit' to move back to the action menu \n >>> "))

                                            if user_input_3[0] == "quit":
                                                loop_control_3 = 1

                                            else:
                                                for key in tdict.keys():
                                                    if user_input_3[0] == str(key):
                                                        user_choice = tdict[key]

                                                loop_control_4 = 0

                                                while loop_control_4 == 0:

                                                    user_input_4 = userInput(input("You have chosen {0}. Do you want to equip it? Type yes or no. \n >>> ".format(user_choice)))

                                                    if user_input_4[0] == "yes":



                                                        player.equipItem(user_choice)


                                                        loop_control_4 = 1
                                                        loop_control_3 = 1

                                                    elif user_input_4[0] == "no":

                                                        loop_control_4 = 1
                                                        loop_control_3 = 1

                                                    else:

                                                        print("Yeah, you said {0} which somehow doesn't make sense. I dunno why, I'm just a program.".format(user_input_4))
                                                                        
                            print("---------------------------------------------------------------------------")
                            time.sleep(5)

                        if rat.c_hp <= 0:
                            print("You slay the rat! Gosh, that must have been so hard!")
                            print("You gain 200 XP for slaying the rat! Congrats! That's a reeeeal accomplishment...")
                            player.add_xp(200)
                            loop_control_2 = 1
                        elif player.c_hp <= 0:
                            print("You were killed by a glorified mouse, congratulations that's really bad. Like REALLY embarassing!\n")
                            print("You now must start this level over, luckily it's not a very long one!")
                            main()


                elif user_input_2[0] == "b" or user_input_2[0] == "my" or user_input_2[0] == "demons":

                    print("You wrestle with your demons, confronting the darker parts of your nature...")
                    res = dice.roll_d20()
                    if res > 17:
                        print("Wow, you successfully face down your demons, you feel lighter, refreshed and generally a more well adjusted person \n")
                        print("which really isn't saying too much. Anyway, you gain 50 XP for your emotional fortitude")
                        player.add_xp(50)

                    else:
                        print("Your demons overtake you, you lay down in the fetal position for a few seconds before recovering and standing back up.")

                    


                
        

                
                           
                                     
        
    


main()
























                    
