class Employee() :
    '''Class that represents an employee'''

    def __init__(self, f_name, l_name, salary) :
        '''Employee instance holds first and last name and salary'''
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self, raise_amount=5000) :
        self.salary += raise_amount