from main import *
from synonym import *
import unittest
f
#author: David Pinos 


# unit tests can be run independently as they dont depend on each others response 

class TestCalc(unittest.TestCase):

    # tests input for response in greeting tag
    def test_greeting(self):
        responses = data['intents'][0]['responses']
        self.assertTrue(get_response("Hi") in responses)


      # tests input for response in goodbye tag
    def test_goodbye(self):
        responses = data['intents'][2]['responses']
        self.assertTrue(get_response("Goodbye") in responses)


    def test_name(self):
        responses2 = data['intents'][4]['responses']
        self.assertTrue(get_response("what is your name") in responses2)


    def test_stress(self):
        responses2 = data['intents'][6]['responses']
        self.assertTrue(get_response("I am stressed") in responses2)


    def test_thanks(self):
        responses2 = data['intents'][9]['responses']
        self.assertTrue(get_response("thank you") in responses2)

    def test_unwell(self):
        responses2 = data['intents'][13]['responses']
        self.assertTrue(get_response("how do I know if im unwell") in responses2)



    # tests input for response in depression tag 
    # test using synonyms 
    def test_depression(self):
        responses2 = data['intents'][3]['responses']
        self.assertTrue(get_response("I am feeling gloomy") in responses2)

    


    

    


if __name__ == '__main__':
    unittest.main()



