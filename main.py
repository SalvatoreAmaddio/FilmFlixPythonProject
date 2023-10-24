from flask import Flask
from menu import *

main = Flask(__name__)
@main.route("/")
def runMenu():
    menu = Menu()
    start = True

    print("Hello and welcome to FilmFlix:")
    while(start):
        menu.displayMain()
        menu.getInput()
        start=menu.getExit()

if __name__ == '__main__':
    main.run()

