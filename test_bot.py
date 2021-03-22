from main import *
import unittest
#author: David Pinos 



class TestCalc(unittest.TestCase):

    # tests input for response in greeting tag
    def test_greeting(self):
        responses = data['intents'][0]['responses']
        self.assertTrue(get_response("Hi") in responses)


      # tests input for response in goodbye tag
    def test_goodbye(self):
        responses = data['intents'][2]['responses']
        self.assertTrue(get_response("Goodbye") in responses)


    # tests input for response in depression tag
    def test_depression(self):
        responses2 = data['intents'][3]['responses']
        self.assertTrue(get_response("I am feeling depressed") in responses2)


        


if __name__ == '__main__':
    unittest.main()



