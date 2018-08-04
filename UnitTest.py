import unittest
from Logger import Logger
class SimpleTest(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        
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
        
if __name__ == '__main__':
    unittest.main()