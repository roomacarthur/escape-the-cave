# import time and sys module for typing effect function.
import sys
import time


# Typing animation function.
def typing(text, speed):
    """
    This is a modified print function,
    rather than the whole print statement appearing all at once,
    the text has a timing in-between characters. In turn this
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
    When user enters a correct option the loops is passed
    and the given path is executed.
    """

    # Consider if the try/except is even needed here
    # as the else statement works fine.
    while True:
        try:
            choice = input(prompt)
            if choice == opt1:
                path1()
                break
            elif choice == opt2:
                path2()
                break
            else:
                print(f"Please enter a valid option! ({opt1} or {opt2})\n")
                continue
        except ValueError:
            print(f"ERROR: please enter a valid option! ({opt1} or {opt2})\n")


def four_choice_option(opt1, opt2, opt3, opt4):
    """
    
    """
    while True:
        choice = int(input("Quickly, which path do you take? (1/2/3/4): \n"))
        try:
            if choice == 1:
                return opt1()
            elif choice == 2:
                return opt2()
            elif choice == 3:
                return opt3()
            elif choice == 4:
                return opt4()
            else:
                print("Please enter a correct option (1/2/3/4).")
                continue
        except ValueError:
            print("You must enter a 'number', try again.")
            continue

# Game over function
def game_over(msg):
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


# Game win function
def game_win(msg):
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
    print("To play again click the 'RUN ESCAPE THE CAVE' button at the top")
