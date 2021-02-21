import unittest
from employee import Employee

class TestEmployee(unittest.TestCase) :
    '''Test for employee class'''

    def setUp(self) :
        '''Create an employee to use for the test methods'''
        self.employee = Employee('Laineys', 'Boo', 100000000)

    def test_give_default_raise(self) :
        '''Test to verify default raise is given'''
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 100005000)

    def test_give_custom_raise(self) :
        '''Test to verify if custom raise is given'''
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 100010000)

unittest.main()