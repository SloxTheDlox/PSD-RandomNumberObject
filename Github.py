import random

class RandomNumbers:
    def __init__(self):
        print("Hello! This programm will find you random numbers")

        self.amount = int(input("Submit how many numbers you want returned: "))
        self.minrange = int(input("What is the lowest number you want? "))
        self.maxrange = int(input("What is the highest range you want? "))

        self.get_random_numbers(self.amount, self.minrange, self.maxrange)

    def get_random_numbers(self, amount, minrange, maxrange):
        for number in range(amount):
            print(random.randint(minrange, maxrange))

testing_tool = RandomNumbers()