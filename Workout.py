import sqlite3
#from datetime import datetime
class DBInterface:
    def __init__(self, DbName):
        print('Initializing Database', DbName)
        self.Queue = list()
        self.dbName = DbName
        self.setTableName = DbName + 'Sets'
        self.workoutTableName = DbName + 'Workouts'
        conn = sqlite3.connect(self.dbName + '.db' )
        c = conn.cursor()
        c.execute('CREATE  TABLE IF NOT EXISTS {0} (name text, reps integer, weight integer, muscles text, date_ TEXT, workoutID integer )'.format(self.setTableName ))
        c.execute('CREATE  TABLE IF NOT EXISTS {0} (workoutID integer PRIMARY KEY, name text, volume integer, avgIntensity integer, date_ TEXT )'.format(self.workoutTableName ))
        
    def QueueSet(self, theSet):
         self.Queue.append(theSet)
    def QueueLevel(self):
         return len(self.Queue)
    def CommitQueue(self):
         conn = sqlite3.connect(self.dbName + '.db')
         c = conn.cursor()
         for item in self.Queue:
               itemTuple = [str(item.Name), int(item.Reps), int(item.Weight), str(item.Muscles), str(item.Date), int(item.ID)]
               try:
                    c.execute('INSERT  INTO  {0} VALUES (?,?,?,?,?,?) '.format( self.setTableName ), itemTuple)
               except:
                     print('Error inserting',itemTuple,' into table')
         conn.commit()
    def ReadSetsDb(self ):
         conn = sqlite3.connect(self.dbName + '.db')
         c = conn.cursor()
         c.execute("SELECT * FROM {0}".format(self.dbName + 'Sets'))
         return c.fetchall()
    def   DeleteSet(self, theSet):
         conn = sqlite3.connect(self.dbName + '.db' )
         c = conn.cursor()
         c.execute("DELETE FROM {0} WHERE date_ =?".format(self.dbName + 'Sets'), (theSet.Date,))
         conn.commit()
    def RemoveSetTable(self):
         conn = sqlite3.connect(self.dbName + '.db' )
         c = conn.cursor()
         c.execute('DROP  TABLE  {0}'.format(self.dbName + 'Sets' ))
         
    def RemoveWorkoutTable(self):
         conn = sqlite3.connect(self.dbName + '.db' )
         c = conn.cursor()
         c.execute('DROP  TABLE  {0}'.format(self.dbName + 'Workouts' ))
class Workout:
   def __init__(self, name, date):
      self.Name = name
      self.Date = date
      self.Exercises = list()
   def calc_Volume(self):
      v = 0
      for set in self.Exercises:
         v = v + set.calcVolume()
         
class Set:
    def __init__(self, Name, Reps, Weight, Muscles, date, ID):
        self.Name = Name
        self.Reps = Reps
        self.Weight = Weight
        self.Muscles = Muscles
        self.Date = date
        self.ID = ID
    def calcVolume(self):
        return self.Reps*self.Weight

    def calcEst1RM(self):
        return int(int(self.Weight * ( 1 + 0.0333*self.Reps))/5)*5
        
    def __str__(self):
         s = 'Name = ' + self.Name + '\n\r'
         s = s + 'Reps = ' + str(self.Reps) + '\n\r'
         s = s + 'Weight = ' + str(self.Weight) + '\n\r'
         s = s + 'Muscles Worked = ' + str(self.Muscles) + '\n\r'
         s = s + 'Date = ' + str(self.Date) + '\n\r'
         s = s + 'WorkoutID = ' + str(self.ID) + '\n\r'
         return s