from database import *
from movie import *
from menu import *

db = Database("FilmFlixPythonProject/filmflix.db")
db.connect()
movie = Movie()
menu = Menu()
start = True

print("Hello and welcome to FilmFlix:")
while(start):
    menu.displayMain()
    menu.getInput()
    start=menu.getExit()


