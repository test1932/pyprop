import pyprop.basicGenerators as bg

# a test
def prop_new1():
    def testingFunc(i, j):
        # print(f'got {i}')
        return True
    return ([bg.intArb(-100, 100), bg.intArb(-100, 100)], testingFunc)

def prop_new2():
    def testingFunc(i, j):
        # print(f'got {i}')
        return True
    return ([bg.intArb(-100, 100), bg.intArb(-100, 100)], testingFunc)