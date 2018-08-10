import sqlite3
class DBInterface:
    def __init__(self, DbName):
        print('Initializing Database', DbName)
        self.Queue = list()
        self.dbName = DbName
        conn = sqlite3.connect(self.dbName + '.db' )
        c = conn.cursor()
        c.execute('CREATE  TABLE IF NOT EXISTS {0} (name text, reps integer, weight integer, muscles text, date_ DATE PRIMARY KEY)'.format(self.dbName ))
    def QueueSet(self, theSet):
         self.Queue.append(theSet)
    def QueueLevel(self):
         return len(self.Queue)
    def CommitQueue(self):
         conn = sqlite3.connect(self.dbName )
         c = conn.cursor()
         for item in self.Queue:
             print('todo')#c.executemany('INSERT  TABLE  {0} '.format(self.dbName ))
    def RemoveTable(self):
         conn = sqlite3.connect(self.dbName )
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
