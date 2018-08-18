import unittest
from Logger import Logger
from Workout import DBInterface
from Workout import Set
from Workout import Workout
import os.path
import time 

#####################################
#   Other tests: mostly for proof of
#   Concept     
#####################################
class SimpleTest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
#####################################
#   Logger tests: mostly for proof of
#   Concept     
#####################################        
class LoggerTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = Logger('Test.log')
    def tearDown(self):        
        self.logger = None
    def test_log(self):
        testString = 'Simple'
        self.logger.log(testString)
        self.logger.stop()
        result = open('Test.log','r').read()        
        self.assertEqual(testString + '\n', result)
    def test_log_complex(self):
        int_ = 0xdeadbeef
        float_ = 3.14159
        string_ = 'This is a more complicated test'
        testString = '{0} {1} {2}'.format(int_, float_, string_)
        self.logger.log(testString)
        self.logger.stop()
        result = open('Test.log','r').read()        
        self.assertEqual(testString + '\n', result)
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LoggerTestCase('test_log'))
        suite.addTest(LoggerTestCase('test_log_complex'))
        return suite        

class WorkoutTestCase(unittest.TestCase):
    def setUp(self):
         self.dbInit = DBInterface('WorkoutHistoryUnitTest')
         self.Workout = Workout('Test', time.strftime('%d%m%Y'))
         self.Workout.Exercises.append(Set('Bench', 5, 140, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y'), 1))
         self.Workout.Exercises.append(Set('Bench', 5, 165, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y'), 1))
         self.Workout.Exercises.append(Set('Bench', 7, 180, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y'), 1))
         self.sets = list()
         self.sets.append(Set('Bench', 5, 140, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y'), 1))
         self.sets.append(Set('Bench', 5, 165, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y'), 1))
         self.sets.append(Set('Bench', 7, 180, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y'), 1))
    def tearDown(self):  
         self.dbInit.RemoveSetTable()
         self.sets = None
         self.dbInit = None
         print('tear down')
    def testDB_Init(self):        
        self.assertTrue(os.path.isfile('WorkoutHistoryUnitTest.db'))
    def test_DB_Queue_Set(self):
         self.dbInit.QueueSet(self.sets[0])
         self.dbInit.QueueSet(self.sets[1])
         self.dbInit.QueueSet(self.sets[2])
         self.assertTrue(self.dbInit.QueueLevel() == 3)
    def test_commit_set(self):
         self.dbInit.QueueSet(self.sets[0])
         self.dbInit.CommitQueue()
         print('The queue is', len(self.dbInit.ReadSetsDb()) )
         self.assertTrue( len(self.dbInit.ReadSetsDb()) == 1)
    def test_commit_set_read_it_back(self):
         self.dbInit.QueueSet(self.sets[0])
         self.dbInit.CommitQueue()
         temp = self.dbInit.ReadSetsDb()
         setFromDb = Set(temp[0][0], temp[0][1], temp[0][2], temp[0][3], temp[0][4], temp[0][5])
         print(self.sets[0])
         print(setFromDb)
         self.assertTrue( setFromDb.Date == self.sets[0].Date)
    def test_remove_set(self):
         self.dbInit.QueueSet(self.sets[0])
         self.dbInit.CommitQueue()
         self.dbInit.DeleteSet(self.sets[0])
         self.assertTrue( len(self.dbInit.ReadSetsDb()) == 0)
    def test_Calc_Volume_Set(self):
         self.sets.append(Set('Bench', 7, 185, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y'), 1))
         # 7 * 185 = 1295
         self.assertTrue( self.sets[-1].calcVolume() == 1295)
    def test_Est_1RM_Set(self):
         self.sets.append(Set('Bench', 7, 200, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y'), 1))
         est1Rm = self.sets[-1].calcEst1RM()
         self.assertTrue( est1Rm == 245)
    def test_Calc_Volume_Workout(self):
         print('The volume of the workout is', self.Workout.calc_Volume())
         self.assertTrue( self.Workout.calc_Volume() == 2785)
if __name__ == '__main__':
    unittest.main()
