# Escape The Cave
# All Code by Ruairidh MacArthur
# https://github.com/roomacarthur
# https://www.linkedin.com/in/ruairidh-macarthur/


# imports:
from functions import typing, two_choice_option
from functions import game_over, game_win, four_choice_option


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
    typing("#######################################\n\n", 0.01)


def start_game():
    """
    Starts the game, retrieves username from player and
    welcomes them to the game.
    """
    # ---WELCOME MESSAGE
    intro_msg()

    # Loop to ensure the user inputs a name.
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
    typing(f"Welcome {P_NAME}, good luck!\n\n", 0.03)
    option_one()


def option_one():
    """
    OPTION 1 function - This is the start of the game,
    where the user makes their initial option on which
    direction to take. If the input is incorrect the input
    will be called again.
    """
    typing("You exit the room through the large wooden door...\n", 0.01)
    typing("You notice the cave goes in two different directions!\n", 0.01)
    # call two_choice function.
    two_choice_option(
        "Do you go left or right? (left/right): \n",
        "left", "right", option_two, option_three)


def option_two():
    """
    OPTION 2 - function, progresses through the story Leading onto
    OPTION 4 no matter the choice.
    If the user decides to pick up the axe, they will have to name
    it and the variable for the axes name has been altered to a
    global variable so it can be called in later functions.
    """
    typing("As you head left the cave gets tighter\n", 0.03)
    typing("you slowly navigate the slippy rocks cautiously...\n\n", 0.03)
    print("WOOOAAAHHH!!!")
    typing("You trip and hit the ground with an almighty bang!\n", 0.03)
    typing("You feel around as you try to get back up and you\n", 0.03)
    typing("realise that you tripped over an axe!\n\n", 0.03)
    # call two_choice function
    two_choice_option(
        "Do you keep the axe? (yes/no): \n", "yes", "no",
        option_four, option_four_one)


def option_three():
    """
    OPTION 3 - the second starting path,
    option of 4 paths all named as integers, each path returns a new function
    and will loop if the value given for 'choice' is not an integer
    """
    typing("You turn right and run as fast as you can!\n\n", 0.01)
    print("SCREEEEEEEEEECHH!!!!\n")
    typing("You find yourself in a massive cavern full of bats!!\n", 0.01)
    typing("The large cavern has 4 exits!\n", 0.01)
    typing("As you ponder on which of the 4 exits to take\n", 0.03)
    typing("you hear some commotion coming from back down the cave! \n", 0.01)
    print(f'"{P_NAME.upper()} IS MAKING A RUN FOR IT!')
    print('GRAB YOUR WEAPONS AND LETS CATCH THEM!!"\n')
    # Call four choice function.
    four_choice_option(option_five, option_six, option_seven, option_twelve)


def option_three_return():
    """
    This allows for the user to return to the option 3 stage
    and get the same options but different textual content.
    """
    print("You end up back in the mahoosive cavern.\n")
    # Call four choice function
    four_choice_option(option_five, option_six, option_seven, option_twelve)


def option_four():
    """
    Option 4 function - If the user has picked up the axe.
    progresses through the story and prompts the user to name their axe.
    prompt the user to input an option to progress further.
    """
    global has_axe
    has_axe = True
    typing("You pick the Axe up, you should give it a name...\n", 0.02)

    while True:
        # set AXE_NAME to a global variable.
        global AXE_NAME
        AXE_NAME = input("What do you want to call it?: \n")

        if AXE_NAME == "":
            print("You really need to give that shiny metal a name...\n")
            continue
        else:
            break
    typing(f"You slide {AXE_NAME} into your belt.\n\n", 0.03)
    typing("As you move deeper, you start to hear some talking.\n", 0.03)
    typing("You come across a door and notice that\n", 0.03)
    typing("the chatter is coming from behind it!\n", 0.03)
    # Call two choice function.
    two_choice_option(
        "Do you have a look behind the door? (yes/no):\n",
        "yes", "no", option_eight, option_nine)


def option_four_one():
    """
    Option 4.1 function - If the user has not picked up the axe.
    The same storyline as option 4 but removes axe story.
    prompt for a two-choice option to continue.
    """
    global has_axe
    has_axe = False
    typing("You leave the axe on the floor and continue onwards\n", 0.03)
    typing("As you move deeper, you start to hear some talking.\n", 0.03)
    typing("You come across a door and notice that\n", 0.03)
    typing("the chatter is coming from behind it!\n", 0.03)
    # Call two choice function.
    two_choice_option(
        "Do you have a look behind the door? (yes/no):\n",
        "yes", "no", option_eight, option_nine)


def option_five():
    """
    OPTION 5 - Continues with story progression,
    prompts the user for two-choice function to progress
    further.
    """
    typing("You picked the largest opening of the four!\n", 0.03)
    typing("You start sprinting as fast as you can,\n", 0.03)
    typing("knowing that the goblins aren't far behind!\n", 0.03)
    typing("All of a sudden you are ankle-deep in the water!\n", 0.03)
    typing("As the water starts to get deeper you start to notice\n", 0.03)
    typing("a faint light at the far end of the cavern!\n", 0.03)
    # Call two choice function.
    two_choice_option(
        "Do you swim or turn around and run? (swim/run): \n",
        "swim", "run", option_thirteen, option_three_return)


def option_six():
    """
    Option 6 - Endpoint of story,
    game_win and prompts users if they would like to play again.
    """
    typing(
        "Oft, you picked the smallest for the four options.\n",
        0.03)
    typing(
        "It's so small, you struggle to fit through the gap!\n",
        0.03)
    typing(
        "You somehow manage to squeeze yourself through.\n",
        0.03)
    typing("You find yourself in a new cavern filled with\n", 0.03)
    typing("slimy reeds that hang from the ceiling.\n", 0.03)
    typing("As you navigate your way through the maze of reeds\n\n", 0.03)
    typing("There is a loud rumble!\n\n", 0.03)
    print("The floor crumbels and gives way!\n")
    typing("AAAGGGGHHHHHHHHH!!!!!!\n\n", 0.03)
    typing("You splash into some water and as you surface\n", 0.03)
    # Call game win function.
    game_win("You realise you have escaped!\n", start_game)


def option_seven():
    """
    OPTION 7 - Progresses through the story and prompt for
    two choice user input to progress further.
    """
    typing(
        "You run straight ahead having to stop suddenly for a massive pit!\n",
        0.03)
    typing(
        "You notice some reeds hanging down from above the pit!\n",
        0.03)
    typing("You can see some light far in the distance over the pit\n", 0.03)
    # Call two choice function
    two_choice_option(
        "Do you risk swinging across? (swing/run): \n", "swing", "run",
        option_seven_one, option_three_return)


def option_seven_one():
    """
    OPTION 7.1 - this is a winning path,
    progress through the story and then call
    the game win function.
    game_win takes the message to show and then calls
    the start_game() function to re-run the game.
    """
    typing("You take a firm grip on one of the reeds...\n", 0.03)
    typing("You pull it back, run and jump!\n", 0.03)
    typing("You successfully land on the other side... somehow...\n\n", 0.03)
    # Call game win function.
    game_win(
        "You continue down the cave and make it outside!\n",
        start_game)


def option_eight():
    """
    OPTION 8 - Progresses through the story but takes
    different paths depending on whether has_axe is
    True or False.
    if True: prompt two choice function and continue
    if False: Prompt game over.
    """
    typing("you slowly ease the door open.\n", 0.03)
    typing(
        "All of a sudden the wind grabs the door and slams it open!\n\n",
        0.03)
    print("BANG!!\n")
    typing("The goblins in the room see you\n", 0.03)
    typing("they advance with their weapons drawn!\n", 0.03)
    if has_axe:
        # Call two choice function.
        two_choice_option(
            "Do you fight or run? (fight/run): \n", "fight", "run",
            option_ten, option_eleven)
    else:
        typing("You turn around and run as fast as you can!\n", 0.03)
        typing(
            "As you sprint the goblins start launching things at you!\n",
            0.03)
        # Call game over function.
        game_over(
            "A large rock cracks you across the back of the head...\n",
            start_game)


def option_nine():
    """
    OPTION 9 - Progresses through the Story dependant on
    weather has_axe is True or False
    has_axe = True: Prompt two choice function and progress
    has_axe = False: Prompt Game over.
    """
    if has_axe:
        # Call two choice function.
        two_choice_option(
            "Do you want to jam your axe in the door? (yes/no): \n",
            "yes", "no", option_nine_one, option_nine_two)
    else:
        # Call game over function
        game_over(
            "A goblin jumps out from a crack in the wall and slaps you silly!",
            start_game)


def option_nine_one():
    """
    OPTION 9.1 - Story progression from Option 9
    call game win function.
    """
    typing("You jam your axe in the door locking it shut!\n", 0.03)
    typing(
        "Whatever is behind the door hears and starts trying to break out!\n",
        0.03)
    typing("the door starts to crack open! YOU RUN!!!!\n\n", 0.03)
    typing("Ohhhh you run as fast as you can!\n", 0.03)
    # Call game win function.
    game_win(
        "You run so fast you make it out of the cave without any harm!\n",
        start_game)


def option_nine_two():
    """
    OPTION 9.2 - progression from Option 9
    continue through story and call game over function.
    """
    typing("You quietly sneak past the door and start to tun again!\n\n", 0.03)
    print("BANG!\n\n")
    typing("The door swings open and two goblins emerge!\n", 0.03)
    typing(
        "Faster than you can turn and run, the goblins fire two arrows!\n",
        0.03)
    # Call game over function.
    game_over(
        "One flies past you & one hits you in the back! You drop dead.\n",
        start_game)


def option_ten():
    """
    OPTION 10 - Progress through the story
    call game over function.
    """
    typing(
        F"You pull {AXE_NAME} from your belt and prepare to fight!\n\n",
        0.03)
    typing(
        "The goblins advance fast... You hold them off as much as you can!\n",
        0.03)
    # Call game over function.
    game_over(
        "As you fight a goblin sneaks up and clubs you over the skull!\n",
        start_game)


def option_eleven():
    """
    OPTION 11 - progress through the story
    call game win function.
    """
    typing(
        f"The goblins start to advance, you pull{AXE_NAME} from your belt!\n",
        0.03)
    typing(
        f"You launch {AXE_NAME} at the large candle chandelier above them!\n",
        0.03)
    typing("Luckily it hits the rope holding it up...\n\n", 0.03)
    print("The chandelier comes crashing down on top of them!\n")
    # Call game win function
    game_win(
        "This slows them down enough for you to make your great escape!\n",
        start_game)


def option_twelve():
    """
    OPTION 12 - progress through the story
    call game over function.
    """
    typing("You make your way down the path which leads to a door.\n", 0.03)
    typing("You slowly reach out and touch the door...\n\n", 0.03)
    print("BANG!!!\n")
    typing(
        "You've triggered a mechanism, closing the door behind you!\n\n",
        0.03)
    print("The large door in front of you slams open..\n")
    # Call game over function
    game_over(
        "you are greeted by a large goblin who clubs you over the head!\n",
        start_game)


def option_thirteen():
    """
    option 13 - progress through the story,
    call game over function.
    """
    typing(
        "You start to swim and the light starts to get brighter!\n",
        0.03)
    typing("OMG! You can see the outside!\n", 0.03)
    typing("Just as you make it past halfway a crocodile grabs your\n", 0.03)
    typing("ankle from under the water and pulls you down!\n\n", 0.03)
    typing("You make a valiant effort to fight off the crocodile...\n", 0.03)
    # Call game over function
    game_over(
        "Unfortunately, you don't succeed\n",
        start_game)

start_game()
