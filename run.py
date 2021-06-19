# python code goes here
import time
import sys

def typing(text):
    """
    This is a modified print function, rather than the whole print statement appearing all at once, the text has a timing in-between characters. In turn this provides a typing like animation. 
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)


typing("Typing animation test.")