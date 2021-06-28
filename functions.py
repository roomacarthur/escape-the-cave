# import time and sys module for typing effect function.
import sys
import time


# Typing animation function.
def typing(text, speed):
    """
    This is a modified print function,
    rather than the whole print statement appearing all at once,
    the text has a timing in-between characters. In turn, this
    provides a typing like animation.
    text = The text you wish to enter.
    speed = The typing animations speed.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


# two choice option function.
def two_choice_option(prompt, opt1, opt2, path1, path2):
    """
    Allows for the input(prompt) of an option(opt1/op2)
    with two outcomes(path1,path2).
    When a user enters a correct option the loop is passed
    and the given path is executed.
    """

    # Consider if the try/except is even needed here
    # as the else statement works fine.
    while True:
        choice = input(prompt)
        if choice == opt1:
            path1()
            break
        elif choice == opt2:
            path2()
            break
        else:
            print()
            print(f"Please enter a valid option! ({opt1} or {opt2})\n")
            continue


def four_choice_option(opt1, opt2, opt3, opt4):
    """
    Function to allow for a 4 point multiple choice option,
    if the input is valid, it will continue with the story.
    If the input is not an integer it will throw a ValueError
    and prompt for input again. If the input is an integer but is not
    valid, it will ask for input again.
    """
    while True:
        choice = input("Quickly, which path do you take? (1/2/3/4): \n")
        try:
            input_int = int(choice)
            if input_int == 1:
                opt1()
                break
            elif input_int == 2:
                opt2()
                break
            elif input_int == 3:
                opt3()
                break
            elif input_int == 4:
                opt4()
                break
            else:
                print("Please enter a correct option (1/2/3/4).")
                continue
        except ValueError:
            print("You must enter a 'number', try again.")


# Game over function
def game_over(msg, function):
    typing(msg, 0.04)
    print()
    typing("         GAME OVER         \n", 0.01)
    typing("███████▀▀▀░░░░░░░▀▀▀███████\n", 0.01)
    typing("████▀░░░░░░░░░░░░░░░░░▀████\n", 0.01)
    typing("███│░░░░░░░░░░░░░░░░░░░│███\n", 0.01)
    typing("██▌│░░░░░░░░░░░░░░░░░░░│▐██\n", 0.01)
    typing("██░└┐░░░░░░░░░░░░░░░░░┌┘░██\n", 0.01)
    typing("██░░└┐░░░░░░░░░░░░░░░┌┘░░██\n", 0.01)
    typing("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n", 0.01)
    typing("██▌░│██████▌░░░▐██████│░▐██\n", 0.01)
    typing("███░│▐███▀▀░░▄░░▀▀███▌│░███\n", 0.01)
    typing("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██\n", 0.01)
    typing("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██\n", 0.01)
    typing("████▄─┘██▌░░░░░░░▐██└─▄████\n", 0.01)
    typing("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████\n", 0.01)
    typing("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████\n", 0.01)
    typing("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████\n", 0.01)
    typing("███████▄░░░░░░░░░░░▄███████\n", 0.01)
    typing("██████████▄▄▄▄▄▄▄██████████\n", 0.01)
    play_again(function)


# Game win function
def game_win(msg, function):
    typing(msg, 0.04)
    print("\n\n")
    typing("#######################################\n", 0.01)
    typing("#     CONGRATULATIONS YOU ESCAPED     #\n", 0.01)
    typing("#                                     #\n", 0.01)
    typing("#          ▄   ▄         ESCAPE       #\n", 0.01)
    typing("#      ▄█▄ █▀█▀█ ▄█▄       THE        #\n", 0.01)
    typing("#     ▀▀████▄█▄████▀▀        CAVE     #\n", 0.01)
    typing("#          ▀█▀█▀                      #\n", 0.01)
    typing("#              By. Ruairidh MacArthur #\n", 0.01)
    typing("#######################################\n", 0.01)
    print()
    play_again(function)


def play_again(option):
    print("To play again click the 'RUN ESCAPE THE CAVE' button at the top\n")
    choice = input("Or simply type 'yes': ")
    if choice == "yes":
        option()
    else:
        print("Thanks for playing!")