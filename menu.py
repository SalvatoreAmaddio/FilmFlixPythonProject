from movie import *
from database import *

class Menu:
    mainMenu=''
    reports=''
    menuSelector=0
    userInput=''
    exit = False
    movie = Movie()
    db = Database("filmflix.db")

    def __init__(self):
        self.db.connect()
        with open("files/MainMenu.txt") as mainMenu:
            self.mainMenu = mainMenu.read()
        with open("files/reports.txt") as reports:
            self.reports = reports.read()

    def displayMain(self):
        self.menuSelector=0
        print(self.mainMenu)

    def runInput(self):
        self.userInput  = input("Please enter an option from above: ")   
        return self.userInput.isnumeric() 

    def getInput(self):
        if (self.runInput()):
            self.goTo()
        else:
            print("Invalid Input")
            self.getInput()

    def getReportInput(self):
        if (self.runInput()):
            self.goToReportOptions()
        else:
            print("Invalid Input")
            self.getReportInput()

    def getExit(self):
        return not self.exit
    
    def back(self):
        self.displayMain()
        self.getInput()

    def nextReportOption(self):
        self.movie.reset()        
        print("")
        print("Please choose another option:")
        print(self.reports)
        self.getReportInput()

    def nextOption(self):
        self.movie.reset()        
        print("")
        print("Please choose another option:")
        self.back()
    
    def checkOutcome(self, outcome,crud):
        if (outcome):
            print(f"Record successfully {crud}!")
        else:
            print("An error has occured. Try again")
            self.goTo()
    
    def confirmDialog(self,msg):
        confirm = input(msg)
        if confirm.upper() == "N": 
           print("Action Aborted")
           self.nextOption()  
           return False
        else:
            return True

    def attemptFetch(self):
        outcome=self.db.selectRecord(self.movie)
        if (outcome==True): return True
        else:
            print("An error has occured. Try again")
            self.goTo()

    def checkInsertedID(self):
        if (self.movie.filmId==0):
            print("The ID you've inserted does not exist")                    
            self.movie.filmId = input("Try again: ")
            self.attemptFetch()
            self.checkInsertedID()
            return False
        else:
            return True

    def goTo(self):
        value = int(self.userInput)
        outcome = False
        match value:
            case 6:
                self.exit=True          
            case 1:
                print("You have selected the Add Record option")
                self.movie.title = input("What is movie title? ")
                self.movie.yearReleased = input("In which year was released? ")
                self.movie.rating = input("what was its rating? ")
                self.movie.duration = input("What is the duration of movie? (express in minutes) ")
                self.movie.genre = input("What genre is the movie? ")
                outcome = self.confirmDialog("Are you sure you want to insert this record? Y/N: ")                                            
                if (outcome==False): return
                outcome = self.db.insertRecord(self.movie)
                self.checkOutcome(outcome,"added")
                self.nextOption()        
            case 2:
                print("You have selected the Delete Record Option")
                self.movie.filmId = input("Please insert the Movie ID: ")
                outcome=self.attemptFetch()
                outcome=self.checkInsertedID()
                outcome = self.confirmDialog("Are you sure you want to delete this record? Y/N: ")                                            
                if (outcome==False): return
                outcome = self.db.deleteRecord(self.movie)
                self.checkOutcome(outcome,"deleted")
                self.nextOption()                               
            case 3:
                print("You have selected the Amend Record record")
                self.movie.filmId = input("Please insert the Movie ID: ")
                outcome=self.attemptFetch()
                outcome=self.checkInsertedID()
                print(f"You have selected the {self.movie.title} movie.")                
                print("What field do you want to amend?")
                self.movie.displayAmendOptions()
                if (self.movie.filmId==0):
                        print("You are going back to the Main Menu")
                        print("")
                        self.back()
                        return
                outcome = self.confirmDialog("Are you sure you want to amend this record? Y/N: ")                                            
                if (outcome==False): return
                outcome = self.db.updateRecord(self.movie)
                self.checkOutcome(outcome,"amended")
                self.nextOption()                               
            case 4:
                print("You have selected the Print all records option")
                print("")
                self.db.printAllRecords("SELECT * FROM tblFilms")
                self.nextOption()                               
            case 5:
                print("You have selected the Report option")
                print("")
                print(self.reports)
                self.getReportInput()
            case _:
                print("The option you've selected is invalid.")
                self.userInput = input("Try again: ")
                self.goTo()

    def goToReportOptions(self):
        value = int(self.userInput)
        outcome = False
        match value:
            case 5:
                self.exit=True
            case 4:
                print("Going back to the Main Menu")    
                print("")
                self.back()          
            case 1:
                    print("Printing all films of a particular genre")  
                    self.movie.genre=input("Please enter the Genre: ")
                    self.db.printAllRecords(f"SELECT * FROM tblFilms WHERE LOWER(genre)='{self.movie.genre.lower()}'")
                    self.nextReportOption()
            case 2:
                    print("Printing all films of a particular year")  
                    self.movie.yearReleased=input("Please enter the Year: ")
                    self.db.printAllRecords(f"SELECT * FROM tblFilms WHERE yearReleased='{self.movie.yearReleased}'")
                    self.nextReportOption()
            case 3:
                    print("Printing all films of a particular rating")                                             
                    self.movie.rating=input("Please enter the Rating: ")
                    self.db.printAllRecords(f"SELECT * FROM tblFilms WHERE LOWER(rating)='{self.movie.rating}'")
                    self.nextReportOption()
            case _:
                print("The option you've selected is invalid.")
                self.userInput = input("Try again: ")
                self.goToReportOptions()


