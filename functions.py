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