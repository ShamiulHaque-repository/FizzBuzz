import sys
import unittest
from model import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    
    fizzbuzz = FizzBuzz()
    
    #Test the stageOne method of FizzBuzz class
    def test_stageOne(self):
        self.assertEqual(self.fizzbuzz.stageOne(3), "Fizz")
        self.assertEqual(self.fizzbuzz.stageOne(5), "Buzz")
        self.assertEqual(self.fizzbuzz.stageOne(15), "FizzBuzz")
        self.assertEqual(self.fizzbuzz.stageOne("10"), False)
        self.assertEqual(self.fizzbuzz.stageOne("Fizz"), False)
        self.assertEqual(self.fizzbuzz.stageOne(15.5), False)

    #Test the stageTwo method of FizzBuzz class
    def test_stageTwo(self):
        self.assertEqual(self.fizzbuzz.stageTwo(3), "Fizz")
        self.assertEqual(self.fizzbuzz.stageTwo(5), "Buzz")
        self.assertEqual(self.fizzbuzz.stageTwo(15), "FizzBuzz")
        self.assertEqual(self.fizzbuzz.stageTwo("10"), False)
        self.assertEqual(self.fizzbuzz.stageTwo("Fizz"), False)
        self.assertEqual(self.fizzbuzz.stageTwo(15.5), False)
        self.assertEqual(self.fizzbuzz.stageTwo(31), "Fizz")
        self.assertEqual(self.fizzbuzz.stageTwo(35), "Buzz")
        self.assertEqual(self.fizzbuzz.stageTwo(37), "Fizz")
        self.assertEqual(self.fizzbuzz.stageTwo(53), "FizzBuzz")
        self.assertEqual(self.fizzbuzz.stageTwo(52), "Buzz")
        self.assertEqual(self.fizzbuzz.stageTwo(57), "Fizz")
        

if __name__ == '__main__':
    unittest.main()

sys.exit()
