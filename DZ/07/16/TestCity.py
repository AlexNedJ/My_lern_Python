import unittest
from  city_country import city_function

class Name_TestCase(unittest.TestCase):
    def test_city_contry(self):
        forma = city_function('santiago', 'chile')
        self.assertEqual(forma, 'Santiago Chile')

    
if __name__ == '__main__':
    unittest.main()
