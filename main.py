import sys
from model import FizzBuzz;

try:
    rangeStart = 1
    rangeEnd = 101
    fizzbuzz = FizzBuzz()

    print("Stage One of FizzBuzz: ")
    for num in range(rangeStart, rangeEnd):
        print(fizzbuzz.stageOne(num))

    print("\nStage Two of FizzBuzz: ")
    for num in range(rangeStart, rangeEnd):
        print(fizzbuzz.stageTwo(num))

except:
    print("Error:", sys.exc_info()[0])

else:
    sys.exit()


