class Movie:
    filmId=0
    title=''
    yearReleased=''
    rating=''
    duration=0
    genre=''
    tableName = 'tblFilms'
    AmendOptions=''
    userInput=0

    def __init__(self):
        with open("files/amendFields.txt") as AmendOptions:
            self.AmendOptions = AmendOptions.read()

    def displayAmendOptions(self):
        print(self.AmendOptions)
        self.userInput = input("Please choose an option from the above: ")
        self.goTo()

    def goTo(self):
        value = int(self.userInput)
        outcome = False
        match value:
            case 1:
                print("You've selected the amend All fields option.")
                self.title = input("The new title is: ")
                self.yearReleased = input("The new year of released is: ")
                self.rating = input("The new rating is: ")
                self.duration = input("The new duration (express in minutes) is: ")
                self.genre = input("The new genre is: ")
            case 2:
                print("You've selected the amend Title field option.")
                self.title = input("The new title is: ")
            case 3:
                print("You've selected the amend Year of Release option.")
                self.yearReleased = input("The new year of released is: ")
            case 4:
                print("You've selected the amend Rating option.")
                self.rating = input("The new rating is: ")
            case 5:
                print("You've selected the amend Duration field option.")
                self.duration = input("The new duration (express in minutes) is: ")
            case 6:
                print("You've selected the amend Genre field option.")
                self.genre = input("The new genre is: ")
            case 7:
                self.filmId=0
                return
            case _:
                print("The option you've selected is invalid.")
                print("Try again.")
                self.userInput = input("Please choose an option from the above: ")
                self.goTo()
        
        if (value>1):
            confirm = input("Do you want to amend further fields? Y/N: ")
            if (confirm.upper()=="Y"):
                print("Select one more field")
                self.displayAmendOptions()

    def get_filmID(self):
        return self.filmId
    
    def get_title(self):
        return self.title
    
    def set_title(self,title):
        self.title=title

    def get_year(self):
        return self.yearReleased
    
    def set_year(self,year):
        self.yearReleased=year

    def get_rating(self):
        return self.rating
    
    def set_rating(self,rating):
        self.rating=rating

    def get_duration(self):
        return self.duration
    
    def set_duration(self,duration):
        self.duration=duration

    def get_genre(self):
        return self.genre
    
    def set_genre(self,genre):
        self.genre=genre

    def __str__(self):
        return f"{self.title}"
    
    def insert(self, cursor, connection):
        try:
            cursor.execute(f'INSERT INTO {self.tableName} VALUES (NULL,?,?,?,?,?)', (self.title, self.yearReleased, self.rating, self.duration, self.genre))
            connection.commit()
            self.filmId = cursor.lastrowid
            return True
        except:
            return False

    def populate(self,tupla):
        self.title=tupla[1]
        self.yearReleased=tupla[2]
        self.rating=tupla[3]
        self.duration=tupla[4] 
        self.genre=tupla[5]                       

    def select(self, cursor, connection):
        try:
            tupla=''
            cursor.execute(f"SELECT * FROM {self.tableName} WHERE filmID = {self.filmId}")
            fetch = cursor.fetchall()
            if len(fetch) == 0:
                self.filmId=0
                return True        
            tupla = fetch[0]
            self.populate(tupla)
            return True
        except:return False    

    def update(self, cursor, connection):
        try:
            cursor.execute(f"UPDATE {self.tableName} SET title = '{self.title}', yearReleased='{self.yearReleased}', rating='{self.rating}', duration='{self.duration}', genre='{self.genre}' WHERE filmID = {self.filmId}")
            connection.commit()
            return True
        except:
            print("I couldn't update the record, help")
            return False

    def delete(self, cursor, connection):
        try:
            cursor.execute(f"DELETE FROM {self.tableName} WHERE filmID = {self.filmId}")
            connection.commit()
            return True
        except:
            return False
        
    def reset(self):
        self.filmId=0
        self.title=''
        self.yearReleased=''
        self.rating=''
        self.duration=0
        self.genre=''