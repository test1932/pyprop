import random
import sys

def intArb(minBound = -sys.maxsize, maxBound = sys.maxsize):
    def gen():
        while True:
            yield random.randint(minBound, maxBound)
    return gen