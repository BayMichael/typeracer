import curses
from curses import wrapper

# Starts the screen, Displays Greeting and Instruction to press a key to advance
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Wilkommen bei dem Tippgeschwindigkeits-Test !")
    stdscr.addstr("\nDrücke eine beliebige Taste um zu starten!")
    stdscr.refresh()
    stdscr.getkey()

# Getting User Key Presses
def wpm_test(stdscr):
    target_text = "Hello World das ist ein Test Text!"
    current_text = []
    
    # If the character is correct append it to current_text
    while True:
        stdscr.clear()
        stdscr.addstr(target_text)

        # If the character is correct, overlay it with green text
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()

        # ASII Value for Esc == 27, if Esc is pressed, breaks the loop
        if ord(key) == 27:
            break
        # If backspace is hit, pop off last char in list
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)

        
# Main Function
# Styling the terminal 
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

# Wrapper is a function imported from curses,
# feeding it with the main function the argument
wrapper(main)