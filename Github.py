import random

class RandomNumbers:
    print("Hello! This programm will find you random numbers")

    def get_random_numbers(amount, minrange, maxrange):
        for number in range(amount):
            print(random.randint(minrange, maxrange))

testing_tool = RandomNumbers
testing_tool.get_random_numbers(3, 22, 24)