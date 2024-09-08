import random


def random_number():
    var = ''
    for item in range(0 , 6):
        num = random.choice(range(0 , 10))
        var += str(num)
    return var
