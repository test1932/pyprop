import pyproptest.basicGenerators as bg

# a test
@bg.test([bg.intArb(-100, 100), bg.intArb(-100, 100)])
def testingFunc(i, j):
    # print(f'got {i}')
    return True

@bg.test([bg.intArb(-100, 100), bg.intArb(-100, 100)])
def testingFunc(i, j):
    # print(f'got {i}')
    return True