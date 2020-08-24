"""
FizzBuzz class implements the logics of both stages of FizzBuzz Kata.

Method stageOne: Implements the first part of the kata where it returns "Fizz" if a number is devisible by 3. 
Returns "Buzz" if devisible by 5. For both it returns "FizzBuzz"

Method stageTwo: Implements the second part of the kata. On top of stageOne, it also returns "Fizz" if a number has 3 in it. 
"Buzz" if a number has 5 in it. "FizzBuzz" if a number contains both 3 and 5 in it.

Both the method returns False if the passed parameter is not an int.
"""
class FizzBuzz:
    
    values = ["FizzBuzz", "Fizz", "Buzz"]

    def stageOne(self, num):
        if not(isinstance(num, int)) : return False
        if num % 3 == 0 and num % 5 == 0 : return self.values[0]
        if num % 3 == 0 : return self.values[1]
        if num % 5 == 0 : return self.values[2]
        return num
    
    def stageTwo(self, num):
        val = self.stageOne(num)
        if val == False : return False
        if val not in self.values:
            if str(3) in str(num) and str(5) in str(num) : return self.values[0]
            if str(3) in str(num) : return self.values[1]
            if str(5) in str(num) : return self.values[2]
        return val