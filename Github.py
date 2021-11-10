import random

def get_random_numbers(amount, minrange, maxrange):
    for number in range(amount):
        print(random.randint(minrange, maxrange))

get_random_numbers(22, 0, 22)