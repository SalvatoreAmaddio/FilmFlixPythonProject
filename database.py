import sqlite3 as sql

class Database:
    connection=''
    connectionString=''
    isConnected=False
    dbCursor=''
    record=''

    def __init__(self, connectionString):
        self.connectionString = connectionString

    def connect(self):
        try:
            self.connection = sql.connect(self.connectionString)     
            self.dbCursor = self.connection.cursor()            
            self.isConnected=True
        except:
            self.isConnected=False
            print("Connection Failed")

    def printAllRecords(self,sql):
        print("")
        self.dbCursor.execute(sql)
        recordset = self.dbCursor.fetchall()
        if len(recordset) == 0:
            print("NO RECORDS")
            return

        for eachrecord in recordset:
            print(eachrecord)

    def selectRecord(self,record):
        return record.select(self.dbCursor,self.connection)

    def insertRecord(self,record):
        return record.insert(self.dbCursor,self.connection)
        
    def deleteRecord(self,record):
        return record.delete(self.dbCursor,self.connection)

    def updateRecord(self,record):
        return record.update(self.dbCursor,self.connection)
