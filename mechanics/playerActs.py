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


move("booger", mode=1)
look("north")

