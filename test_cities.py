import unittest
from city_functions import format_city_country

class TestCityCountry(unittest.TestCase) :
    '''Tests city_functions.py'''

    def test_city_country(self) :
        '''Do city country pairings like santiago chile work?'''
        formatted_city_country = format_city_country('santiago', 'chile')

        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self) :
        '''Do city country poplation groupings like santiago chile 5000000 work?'''
        formatted_city_country_pop = format_city_country('santiago', 'chile', '5000000')

        self.assertEqual(formatted_city_country_pop, 'Santiago, Chile - Population 5000000')

unittest.main()