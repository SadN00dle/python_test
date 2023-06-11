import curses
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to typing test!\n")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "This is the test for typing test! please feel free to review the app"
    current_text = []

    stdscr.clear()
    stdscr.addstr(target_text)

    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)

    start_screen(stdscr)
    wpm_test(stdscr)
wrapper(main)
