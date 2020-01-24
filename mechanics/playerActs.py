# File that contains all of the basic player actions aka ones that the player can ALWAYS do unless restricted by something
"""
Feature List:
- Look
    -West
    -East
    -Up
    -Down
    -North
    -South

- Move
    -South
    -North
    -East
    -West

- Search the ground
- Skills tests
    -acrobatics
    -appraise
    -bluff
    -climb
    -craft
    -diplomacy
    -disable device
    -disguise
    -escape artist
    -heal
    -intimidate
    -knowledge
    -linguistics
    -perception
    -perform
    -ride
    -sense motive
    -sleight of hand
    -spellcraft
    -stealth
    -survival
    -swim
    -persuade
    -strength
    
    -
"""

import diceRolling as roll
from time import sleep

def look(direction, flavor=" and see nothing of note, if you're seeing this message then someone didn't write in the flavor text properly...\n"):
    print("You look to the " + direction + flavor + ".\n")

def move(direction, flavor=" and nothing much interesting happens to you, ah the boring life", player=None, mode=0): #mode=0 indicates story mode
    if mode == 0:
        print("You walk " + direction + flavor + ".\n")
    elif mode == 1:
        print("You move one square " + direction + ".\n")
        if direction == "south":
            player.move_south()
        elif direction == "north":
            player.move_north()
        elif direction == "east":
            player.move_north()
        elif direction == "west":
            player.move_north()
        else:
            raise ValueError("The value input to direction made no sense. value: " + direction)

def skill_test(skill, dif=10, obj=None):
    
    if skill == "disable device" and obj is not None:
        print("You attempt to use your knowledge of devices to disable this " + obj.desc + ".\n")
        score = roll.roll_d20()
        if score >= obj.dif:
            print("Success! " + obj.success + ".\n")
        else:
            print("Sorry, you failed your skill check...basically you suck. lolz")

    elif skill == "disable device" and obj is None:
        print("I don't think you can do that...can you really disable that device?")
        
    if skill == "climb" and obj is not None:
        print("You attempt to climb the " + obj.desc + ".\n")
        score = roll.roll_d20()
        if score >= obj.dif:
            print("Success! " + obj.success + ".\n")
        else:
            print("Oof, you fall down the " + obj.desc + " and take " + obj.dmg + " damage.\n")
            dmg = roll.roll_management(obj.dmg)
            return dmg

        
    elif skill == "climb" and obj is None:
        print("What are you trying to climb? I didn't understand that...(probably not implemented by the lazy devs)")

# class lock():

#     dif = 15
#     success = "The lock springs open!"
#     desc = "shiny black lock"  

# class ladder():

#     dif = 15
#     success = "You climb the ladder, wow, do you feel accomplished? psh"
#     desc = "rickety ladder"
#     dmg = "1d4"

# new_ladder = ladder()
# dmg = skill_test("climb", obj=new_ladder)

# print(dmg)
