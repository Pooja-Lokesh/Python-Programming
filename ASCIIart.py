#A program to get a text as input from user and print it in following font with the color user asks to -
# _   _              _   _
#| |_| |/ _ \ | | | | __| '_ \ / _ \ '__/ _ \
#|  _  |  __/ |_| | | |_| | | |  __/ | |  __/
#|_| |_|\___|\__, |  \__|_| |_|\___|_|  \___|
#            |___/
#This program also is an example for external module importing and installing.

from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ('blue','red','yellow','green','cyan','magenta')

def print_art(msg, color):
    if color not in valid_colors :
       color = 'magenta'
    ascii_art = figlet_format(msg)
    color_ascii = colored(ascii_art, color=color)
    print(color_ascii)

msg = input("Enter the message to be printed :")
color = input("Enter the color of the text :")
print_art(msg,color)
