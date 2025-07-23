import unittest
from worker import Employ
class TestWorker(unittest.TestCase):
    def setUp(self):
        self.my_person = Employ('Aleksndr', 'Nedov', 2000)
    
    def test_give_defaul_raise(self):
        self.my_person.give_rise()
        self.assertEqual(self.my_person.otklad, 7000)
    
    def test_give_custom_raise(self):
        self.my_person.give_rise(10000)
        self.assertEqual(self.my_person.otklad, 12000)

if __name__ == '__main__':
    unittest.main()