import diceRolling
import playerChar
import parse
import world

def userInput(user_input):
    return user_input.lower().split(" ")

def main():
    openingText()

    name = input("What is your name? If you don't answer, it'll be set to a default name which is pretty stupid so you may as well put something down...  \n \nEnter your name: ")
    print("\n")
    
    player = playerChar.newPC(world.Cavern())
    if name != "":
        player.change_name(name)
    print("Hi " + player.char_name + "\n")
    
    playing = True

    while playing:
        print("What do you want to do?")
        
        user_input = userInput(input("\n >>> "))

        print()
        
        [x.lower() for x in user_input]

        syntax = parse.parseInput(user_input)

        if not syntax:
            print("What the hell! You didn't say anything that makes sense! Try again, dummy. \n")

        try:
            action_method = getattr(player, syntax.verb)
            action_method(syntax.noun)
        except AttributeError:
            print("I don't recognize that command. Try again.")
        


def openingText():

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

main()