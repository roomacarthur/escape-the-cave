# python code goes here
import time
import sys


# Typing animation function.
def typing(text, speed):
    """
    This is a modified print function, rather than the whole print statement appearing all at once, the text has a timing in-between characters. In turn this provides a typing like animation. 
    text = The text you wish to enter.
    speed = The typing animations speed.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def intro_msg():
    """
    Simple function to print the welcome graphics, this will be used more than once so to keep code readable it's going in it's own function.
    """
    print()
    typing("#####################################\n", 0.01)
    typing("#                                   #\n", 0.01)
    typing("#        ▄   ▄         ESCAPE       #\n", 0.01)
    typing("#    ▄█▄ █▀█▀█ ▄█▄       THE        #\n", 0.01)
    typing("#   ▀▀████▄█▄████▀▀        CAVE     #\n", 0.01)
    typing("#        ▀█▀█▀                      #\n", 0.01)
    typing("#                           By. Roo #\n", 0.01)
    typing("#####################################\n", 0.01)
    print()
# Start quiz function.
def start_game():
    """
    Starts the game, retrieves username from player and welcomes them to the game. 
    """
    # ---WELCOME MESSAGE
    intro_msg()
    
    p_name = input("Please enter a username: \n")

    inv_slots = 2
    typing(f"Welcome {p_name}, good luck and remember you only have {inv_slots} bag spaces!\n", 0.03)
    option_one()

def option_one():
    """
    First player option for the game. 
    """
    typing("You slowly open the door to find the cave leads in two different directions...\n", 0.03)
    choice_one = input("Do you go left or right? (left/right): ")
    if choice_one.lower() == "left":
        typing("You slowly close the door behind you and head left down the dark dave...", 0.03)
        typing("As you slowly navigate the cave you see a light in the distance.", 0.03)
    elif choice_one.lower() == "right":
        print()
    else:
        print()


start_game()