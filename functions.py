# import time and sys module for typing effect function.
import sys
import time

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

# two choice option function.
def two_choice_option(prompt,opt1,opt2,path1,path2):
    """
    Allows for the input(prompt) of an option(opt1/op2) with two outcomes(path1,path2).
    When user enters a correct option the loops is passed and the given path is executed.
    
    """

    # Consider if the try/except is even needed here as the else statement works fine. 
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

# Game over function

def game_over(msg):
    typing(msg,0.04)
    print("         GAME OVER         ")
    print("███████▀▀▀░░░░░░░▀▀▀███████")
    print("████▀░░░░░░░░░░░░░░░░░▀████")
    print("███│░░░░░░░░░░░░░░░░░░░│███")
    print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
    print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
    print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
    print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
    print("██▌░│██████▌░░░▐██████│░▐██")
    print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
    print("██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
    print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
    print("████▄─┘██▌░░░░░░░▐██└─▄████")
    print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
    print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
    print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
    print("███████▄░░░░░░░░░░░▄███████")
    print("██████████▄▄▄▄▄▄▄██████████")
