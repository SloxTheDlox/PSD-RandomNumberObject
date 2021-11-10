import random

#Preconditions: User must input something, they cannot be blank spaces; 
#Inputs must be valid integers
#Postconditions: The program shall generate the number of random numbers requested; 
#The program must print out these numbers, and display them to the user

class RandomNumbers:
    def __init__(self):
        print("Hello! This programm will find you random numbers")

        try:
            self.amount = int(input("Submit how many numbers you want returned: "))
            self.minrange = int(input("What is the lowest number you want? "))
            self.maxrange = int(input("What is the highest range you want? "))

            self.get_random_numbers(self.amount, self.minrange, self.maxrange)
        except:
            print("Error all input should be an integer. Try again.")     

    def get_random_numbers(self, amount, minrange, maxrange):
        for number in range(amount):
            print(random.randint(minrange, maxrange))

testing_tool = RandomNumbers()