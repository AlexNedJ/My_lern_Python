import unittest 
from survey import Anonymous_Survey
class Test_Anonimus_Survey(unittest.TestCase):
    def setUp(self):
        question = "what language did your first learn to speak?"
        self.my_servey = Anonymous_Survey(question)
        self.responses =['English', 'Spanish', 'Mondarian']

    def test_store_singl_response(self):
        self.my_servey.stor_respones(self.responses[0])
        self.assertIn(self.responses[0], self.my_servey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_servey.stor_respones(response)
            
        for response in self.responses:
            self.assertIn(response, self.my_servey.responses)

if __name__ == '__main__':
    unittest.main()