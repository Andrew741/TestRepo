import sqlite3
class DBInterface:
    def __init__(self):
        print('Initializing Database')
        conn = sqlite3.connect('WorkoutHistory.db')
        c = conn.cursor()
        c.execute('CREATE IF NOT EXIST WorkoutHistory (name text, reps integer, weight integer, muscles text)')
        
class Set:
    def __init__(self, Name, Reps, Weight, Muscles):
        self.Name = Name
        self.Reps = Reps
        self.Weight = Weight
        self.Muscles = Muscles

    def calcVolume(self):
        return self.Reps*self.Weight

    def calcEst1RM(self):
        return self.Weight * ( 1 + 0.0333*self.Reps)

    def commitToDB(self):
        print('TO DO')
