# python code goes here
from functions import typing

def intro_msg():
    """
    Simple function to print the welcome graphics, this will be used more than once so to keep code readable it's going in it's own function.
    """
    print()
    # typing("#####################################\n", 0.01)
    # typing("#                                   #\n", 0.01)
    # typing("#        ▄   ▄         ESCAPE       #\n", 0.01)
    # typing("#    ▄█▄ █▀█▀█ ▄█▄       THE        #\n", 0.01)
    # typing("#   ▀▀████▄█▄████▀▀        CAVE     #\n", 0.01)
    # typing("#        ▀█▀█▀                      #\n", 0.01)
    # typing("#                           By. Roo #\n", 0.01)
    # typing("#####################################\n", 0.01)
    # print()
# Start quiz function.
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
        if P_NAME == "":
            print("You need to enter a username to continue...\n")
            continue
        else:
            break
    typing(f"Welcome {P_NAME}, good luck!\n", 0.03)
    option_one()

def option_one():
    typing("You exit the room through the large wooden door and you notice the cave goes in two different directions!\n",0.01)
    while True:
        choice = input("Do you go left or right? (left/right): ")
        if choice == "left":
            option_two()
            break
        elif choice == "right":
            option_three()
            break
        elif (choice == "") or(choice != "left") or (choice != "right"):
            print("please enter a correct option. (left or right)")
            continue
        else:
            break

def option_two():
    """
    OPTION 2 - function, progresses through the story Leading onto OPTION 4 no matter the choice. 
    If the user decides to pick up the axe, they will have to name it and the variable for the axes name has been altered to a global variable so it can be called in later functions. 
    """

    typing("As you head left the cave gets tighter, so you slowly navigate the slippy rocks cautiously...\n",0.03)
    print("WOOOAAAHHH!!! You trip and hit the ground with an almighty bang!\n")
    typing("You feel around as you try to get back up and realise that you tripped over an axe!\n", 0.03)
    while True:
        choice = input("Do you keep the axe? (yes/no): ")
        if choice == "yes":
            typing("Ok then, If you want to keep it, it will need a name!\n",0.03)
            global AXE_NAME
            AXE_NAME = input("What do you want to call the axe?: ")
            typing(f"{AXE_NAME}, Is a very wise choice!\n",0.03)
            option_four()
            break
        elif choice == "no":
            option_four()
            break
        elif choice == "" and choice != ("yes") or ("no"):
            print("please enter a valid option! (yes or no)\n")
            continue
        else:
            break

def option_three():
    typing("option 3",0.03)

def option_four():
    typing("option 4",0.03)

start_game()
