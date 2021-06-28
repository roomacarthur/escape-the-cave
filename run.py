# Escape The Cave
# All Code by Ruairidh MacArthur
# https://github.com/roomacarthur
# https://www.linkedin.com/in/ruairidh-macarthur/


# imports:
from functions import typing, two_choice_option, game_over, game_win, four_choice_option

def intro_msg():
    """
    Simple function to print the welcome graphics, this will be
    used more than once so to keep code readable it's going in
    it's own function.
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
    Starts the game, retrieves username from player and
    welcomes them to the game.
    """
    # ---WELCOME MESSAGE
    intro_msg()

    # Loop the name input call to ensure that the user inputs a name.
    while True:
        # set P_NAME to a global variable.
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
    OPTION 1 function - This is the start of the game,
    where the user makes their initial option on which
    direction to take. If input is incorrect the input
    will be called again.
    """
    typing("You exit the room through the large wooden door and you notice the cave goes in two different directions!\n", 0.01)
    # call two_choice function.
    two_choice_option("Do you go left or right? (left/right): \n", "left", "right", option_two, option_three)


def option_two():
    """
    OPTION 2 - function, progresses through the story Leading onto
    OPTION 4 no matter the choice.
    If the user decides to pick up the axe, they will have to name
    it and the variable for the axes name has been altered to a
    global variable so it can be called in later functions.
    """
    typing("As you head left the cave gets tighter, so you slowly navigate the slippy rocks cautiously...\n", 0.03)
    print("WOOOAAAHHH!!! You trip and hit the ground with an almighty bang!\n")
    typing("You feel around as you try to get back up and realise that you tripped over an axe!\n", 0.03)
    # call two_choice function
    two_choice_option("Do you keep the axe? (yes/no): \n", "yes", "no", option_four, option_four_one)


def option_three():
    """
    OPTION 3 - the second starting path,
    option of 4 paths all named as integers, each path returns a new function
    and will loop if the value given for 'choice' is not an integer
    """
    typing("You turn right and run as fast as you can!\n\n", 0.01)
    print("SCREEEEEEEEEECHH!!!!\n\n")
    typing("WOAHH! You find yourself in a massive cavern full of bats!!\n", 0.01)
    typing("The large cavern has 4 exits!\n", 0.01)
    typing("As you ponder on which of the 4 exits to take you hear some commotion coming from back down the cave! \n", 0.01)
    print(f'" IS MAKING A RUN FOR IT! GRAB YOUR WEAPONS AND LETS CATCH THEM!!"\n')
    four_choice_option(option_five, option_six, option_seven, option_twelve)


def option_three_return():
    print("You end up back in the mahoosive cavern.\n")
    four_choice_option(option_five, option_six, option_seven, option_twelve)

def option_four():
    """
    Option 4 function - If user has picked up axe.
    progresses through the story and prompts the user to name their axe.
    prompt the user to input an option to progress further.
    """
    global has_axe
    has_axe = True
    typing("You pick the Axe up, you should give it a name..\n", 0.02)
    global AXE_NAME
    AXE_NAME = input("What do you want to call it?: \n")
    typing(f"You slide {AXE_NAME} into your belt and continue moving down the cave.\n", 0.03)
    typing("As you move deeper into the cave you start to hear some talking coming from somewhere\n", 0.03)
    typing("You come across a door and notice that the chatter is coming from behind it!\n", 0.03)
    two_choice_option("Do you have a look behind the door? (yes/no):\n", "yes", "no", option_eight, option_nine)


def option_four_one():
    """
    Option 4.1 function - If user has not picked up axe.
    """
    typing("You leave the axe on the floor and move deeper into the cave system!\n", 0.03)
    typing("You can hear some chatter coming from further down the cave\n", 0.03)
    typing("You come across a door and notice that the chatter is coming from behind it!\n", 0.03)
    two_choice_option("Do you have a look behind the door? (yes/no):\n", "yes", "no", option_eight, option_nine)


def option_five():
    typing("You picked the largest opening of the four!\n", 0.03)
    typing("You start sprinting as fast as you can, knowing that the goblins aren't far behind!\n", 0.03)
    typing("All of a sudden you are ankle deep in water!\n", 0.03)
    typing("As the water starts to get deeper but you notice a faint light at the far end of the cavern!\n", 0.03)
    two_choice_option("Do you swim or turn around and run? (swim/run): \n", "swim", "run", option_thirteen, option_three_return)


# OPTION 6
def option_six():
    typing("option 6", 0.03)


# OPTION 7
def option_seven():
    typing("option 7", 0.03)


# OPTION 8
def option_eight():
    typing("you slowly ease the door open.\n", 0.03)
    typing("All of a sudden a gust of wind grabs the door and slams it open!\n\n", 0.03)
    print("BANG!!\n\n")
    typing("The goblins in the room see you and advance with their weapons drawn!\n", 0.03)
    if has_axe == True:
        two_choice_option("Do you fight or run? (fight/run): \n", "fight", "run", option_ten, option_eleven)
    else:
        typing("You turn around and run as fast as you can!\n", 0.03)
        typing("As you make a break for it the goblins start launching things at you!\n", 0.03)
        game_over("A large rock cracks you across the back of the head....\n")

# OPTION 9
def option_nine():
    if has_axe == True:
        print("has axe")
    else:    
        typing("no axe", 0.03)


# OPTION 10
def option_ten():
    typing("option 10", 0.03)


# OPTION 11
def option_eleven():
    typing(f"The goblins start to advance quickly, you pull{AXE_NAME} from your belt!\n", 0.03)
    typing(f"You launch {AXE_NAME} at the massive candle chandelier above the goblins!\n", 0.03)
    typing(f"Luckily it hits the rope holding it up and the chandelier comes crashing down on top of them!\n", 0.03)
    # Game Win message
    game_win("This slows them down enough for you to make your great escape!\n")


# OPTION 12
def option_twelve():
    typing("You make your way down the path which leads to a door.\n", 0.03)
    typing("You slowly reach out and touch the door...\n\n", 0.03)
    print("BANG!!!\n\n")
    typing("You've triggered a mechanism, closing the door behind you!\n", 0.03)
    # Game Over message
    game_over("The door in front of you opens and you are greeted by a large goblin who clubs you over the head!\n")


# OPTION 13
def option_thirteen():
    typing("You start to swim and the light starts to get brighter!\n", 0.03)
    typing("OMG! You can see the outside!\n", 0.03)
    typing("Just as you make it past halfway a crocodile grabs your ankle from under the water and pulls you down!\n", 0.05)
    print()
    # Game Over message
    game_over("You make a valiant effort to fight the crocodile off, unfortunately you don't succeed\n")


# OPTION 14
def option_fourteen():
    typing("option 14", 0.03)


start_game()
# option_two()




