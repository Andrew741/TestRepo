import sqlite3
class DBInterface:
    def __init__(self):
        print('Initializing Database')
        self.Queue = list()
        conn = sqlite3.connect('WorkoutHistory.db')
        c = conn.cursor()
        c.execute('CREATE  TABLE IF NOT EXISTS WorkoutHistory (name text, reps integer, weight integer, muscles text, date_ DATE PRIMARY KEY)')
    def QueueSet(self, theSets):
         for set in theSets:
            self.Queue.append(set)
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
