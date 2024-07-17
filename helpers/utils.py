import random

def get_random_top_skip():
    top = random.randint(1, 200)
    skip = random.randint(0, 5000)
    return top, skip
