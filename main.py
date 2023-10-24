from menu import *

menu = Menu()
start = True

print("Hello and welcome to FilmFlix:")
while(start):
    menu.displayMain()
    menu.getInput()
    start=menu.getExit()


