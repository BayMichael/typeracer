import curses
from curses import wrapper

# Main Function
def main(stdscr):

    stdscr.clear()
    stdscr.addstr("Hello World")
    stdscr.refresh()
    stdscr.getkey()

# Wrapper is a function imported from curses,
# feeding it with the main function the argument
wrapper(main)