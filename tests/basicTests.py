import sys
import random
import pyprop.basicGenerators as bg

# a test
def prop_new():
    def testingFunc(i, j):
        # print(f'got {i}')
        return True
    return ([bg.intArb(-100, 100), bg.intArb(-100, 100)], testingFunc)