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

# Start quiz function.
def start_game():
    """
    Starts the game, retrieves username from player and welcomes them to the game. 
    """
    # ---WELCOME MESSAGE
    p_name = input("Please enter a username: \n")
    inv_slots = 2
    typing(f"Welcome {p_name}, good luck and remember you only have {inv_slots} bag spaces!\n", 0.03)

start_game()