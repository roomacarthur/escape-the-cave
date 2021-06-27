# Escape The Cave
# All Code by Ruairidh MacArthur
# https://github.com/roomacarthur
# https://www.linkedin.com/in/ruairidh-macarthur/


# imports:
from functions import typing, two_choice_option

def intro_msg():
    """
    Simple function to print the welcome graphics, this will be used more than once so to keep code readable it's going in it's own function.
    """
    print()
    typing("#######################################\n", 0.01)
    typing("#                                     #\n", 0.01)
    typing("#          ▄   ▄         ESCAPE       #\n", 0.01)
    typing("#      ▄█▄ █▀█▀█ ▄█▄       THE        #\n", 0.01)
    typing("#     ▀▀████▄█▄████▀▀        CAVE     #\n", 0.01)
    typing("#          ▀█▀█▀                      #\n", 0.01)
    typing("#              By. Ruairidh MacArthur #\n", 0.01)
    typing("#######################################\n", 0.01)
    print()

def start_game():
    """
    Starts the game, retrieves username from player and welcomes them to the game. 
    """
    # ---WELCOME MESSAGE
    intro_msg()

    # Loop the name input call to ensure that the user inputs a name. 
    while True:
        #set P_NAME to a global variable so it can be called in other situations.
        global P_NAME
        P_NAME = input("Please enter a username: \n")
        print()
        if P_NAME == "":
            print("You need to enter a username to continue...\n")
            continue
        else:
            break
    typing(f"Welcome {P_NAME}, good luck!\n", 0.03)
    print("................")
    option_one()

def option_one():
    """
    OPTION 1 function - This is the start of the game, where the user makes their initial option on which direction to take. 
    If input is incorrect the input will be called again.
    """
    typing("You exit the room through the large wooden door and you notice the cave goes in two different directions!\n",0.01)
    print()
    # call two_choice function.
    two_choice_option("Do you go left or right? (left/right): ", "left", "right", option_two, option_three)

def option_two():
    """
    OPTION 2 - function, progresses through the story Leading onto OPTION 4 no matter the choice. 
    If the user decides to pick up the axe, they will have to name it and the variable for the axes name has been altered to a global variable so it can be called in later functions. 
    """

    typing("As you head left the cave gets tighter, so you slowly navigate the slippy rocks cautiously...\n",0.03)
    print()
    print("WOOOAAAHHH!!! You trip and hit the ground with an almighty bang!\n")
    typing("You feel around as you try to get back up and realise that you tripped over an axe!\n", 0.03)
    two_choice_option("Do you keep the axe? (yes/no): ","yes","no",option_four,option_four)

def option_three():
    """
    OPTION 3 - the second starting path, option of 4 paths all named as integers, each path returns a new function and will loop if the value given for 'choice' is not an integer
    """
    typing("You turn right and run as fast as you can!\n",0.01)
    print()
    print("SCREEEEEEEEEECHH!!!!\n")
    typing("WOAHH! You find yourself in a massive cavern full of bats!!\n",0.01)
    print()
    typing("The large cavern has 4 exits!\n",0.01)
    print()
    typing("As you ponder on which of the 4 exits to take you hear some commotion coming from back down the cave! \n",0.01)
    print()
    print(f'" IS MAKING A RUN FOR IT! GRAB YOUR WEAPONS AND LETS CATCH THEM!!"\n')
    
    while True:
        choice = int(input("Quickly, which path do you take? (1/2/3/4): "))
        try:
            if choice == 1:
                return option_five()
            elif choice == 2:
                return option_six()
            elif choice == 3:
                return option_seven()
            elif choice == 4:
                return option_twelve()
            else:
                print("Please enter a correct option (1/2/3/4).")
                continue
        except ValueError:
            print("You must enter a 'number', try again.")
            continue
            
        


def option_four():
    print("option 4")
def option_five():
    typing("option 5",0.03)
def option_six():
    typing("option 6",0.03)
def option_seven():
    typing("option 7",0.03)
def option_eight():
    typing("option 8",0.03)
def option_nine():
    typing("option 9",0.03)
def option_ten():
    typing("option 10",0.03)
def option_eleven():
    typing("option 11",0.03)
def option_twelve():
    typing("option 12",0.03)
def option_thirteen():
    typing("option 13",0.03)

start_game()



