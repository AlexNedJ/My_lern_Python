import unittest 
from name_funcions import get_formadet_name
class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        format_name = get_formadet_name("janis", "joplin") 
        self.assertEqual(format_name, 'Janis Joplin')

    def test_first_last_midl_name(self):
        formated_name = get_formadet_name("woolfgran", "mozart", "amadeus")
        self.assertEqual(formated_name, 'Woolfgran Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()