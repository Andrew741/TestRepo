import sqlite3
#from datetime import datetime
class DBInterface:
    def __init__(self, DbName):
        print('Initializing Database', DbName)
        self.Queue = list()
        self.dbName = DbName
        conn = sqlite3.connect(self.dbName + '.db' )
        c = conn.cursor()
        c.execute('CREATE  TABLE IF NOT EXISTS {0} (name text, reps integer, weight integer, muscles text, date_ TEXT PRIMARY KEY)'.format(self.dbName ))
    def QueueSet(self, theSet):
         self.Queue.append(theSet)
    def QueueLevel(self):
         return len(self.Queue)
    def CommitQueue(self):
         conn = sqlite3.connect(self.dbName + '.db')
         c = conn.cursor()
         for item in self.Queue:
               itemTuple = [str(item.Name), int(item.Reps), int(item.Weight), str(item.Muscles), str(item.Date)]
               try:
                    c.execute('INSERT  INTO  {0} VALUES (?,?,?,?,?) '.format(self.dbName ), itemTuple)
               except:
                     print('Error inserting into table')
         conn.commit()
    def ReadDb(self):
         conn = sqlite3.connect(self.dbName + '.db')
         c = conn.cursor()
         c.execute("SELECT * FROM {0}".format(self.dbName))
         return c.fetchall()
         
    def RemoveTable(self):
         conn = sqlite3.connect(self.dbName + '.db' )
         c = conn.cursor()
         c.execute('DROP  TABLE  {0} '.format(self.dbName ))
class Set:
    def __init__(self, Name, Reps, Weight, Muscles, date):
        self.Name = Name
        self.Reps = Reps
        self.Weight = Weight
        self.Muscles = Muscles
        self.Date = date
    def calcVolume(self):
        return self.Reps*self.Weight

    def calcEst1RM(self):
        return self.Weight * ( 1 + 0.0333*self.Reps)

    def commitToDB(self):
        print('TO DO')
