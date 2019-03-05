Title: Python - colorized text in terminal
Date: 2016-06-27 15:17:58
Category: Python
Tags: python, terminal
Summary: This snippet is useful if you want to make your terminal output colorized.


This snippet is useful if you want to make your terminal output
colorized. It should work on Unix and Windows with
[ANSI.SYS](https://support.microsoft.com/cs-cz/kb/101875) enabled.

	:::python
    class colors():
		# Text mode
        ENDC      = '\033[0m'
        BOLD      = '\033[1m'
        UNDERLINE = '\033[4m'
		INVERSE   = '\033[7m'

		# Colors
        ORANGE    = '\033[93m'
        BLACK     = '\033[0;30m'
        BLUE      = '\033[0;34m'
        GREEN     = '\033[0;32m'
        CYAN      = '\033[0;36m'
        RED       = '\033[0;31m'
        PURPLE    = '\033[0;35m'
        BROWN     = '\033[0;33m'
        LGRAY     = '\033[0;37m'
        DGRAY     = '\033[1;30m'
        LBLUE     = '\033[1;34m'
        LGREEN    = '\033[1;32m'
        LCYAN     = '\033[1;36m'
        LRED      = '\033[1;31m'
        LPURPLE   = '\033[1;35m'
        YELLOW    = '\033[1;33m'
        WHITE     = '\033[1;37m'

You can combine colors and text modes, for example, this command will
print red, underlined text:

	:::python
    print(colors.RED + colors.UNDERLINE + 'hello world' + colors.ENDC)

Note: Do not forget to add `colors.ENDC` at the end, otherwise the
rest of the output will be colorized.
