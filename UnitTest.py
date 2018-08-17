import unittest
from Logger import Logger
from Workout import DBInterface
from Workout import Set
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
         self.sets = list()
         self.sets.append(Set('Bench', 5, 140, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y')))
         #self.sets.append(Set('Bench', 5, 140, 'Chest, Shoulders, Arms', time.strftime('%d%m%Y')))
    def tearDown(self):  
         self.dbInit.RemoveTable()
         self.sets = None
         self.dbInit = None
         print('tear down')
    def testDB_Init(self):        
        self.assertTrue(os.path.isfile('WorkoutHistoryUnitTest.db'))
    def test_DB_Queue_Set(self):
         self.dbInit.QueueSet(self.sets[0])
         self.assertTrue(self.dbInit.QueueLevel() == 1)
    def test_commit_set(self):
         self.dbInit.QueueSet(self.sets[0])
         self.dbInit.CommitQueue()
         self.assertTrue( len(self.dbInit.ReadDb()) == 1)
    def test_commit_set_read_it_back(self):
         self.dbInit.QueueSet(self.sets[0])
         self.dbInit.CommitQueue()
         temp = self.dbInit.ReadDb()
         setFromDb = Set(temp[0][0], temp[0][1], temp[0][2], temp[0][3], temp[0][4])
         print(self.sets[0])
         print(setFromDb)
         self.assertTrue( setFromDb.Date == self.sets[0].Date)
if __name__ == '__main__':
    unittest.main()
