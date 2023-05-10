from inspect import getmembers, isfunction, getfullargspec
import sys
import re
    

class tester:
    """
    class for creating testing objects to test modules.
    """
    def __init__(self, module, nameStruct = "prop_", iters = 100) -> None:
        """
        constructor method.
        """
        self.setModule(module)
        self.setPattern(nameStruct)
        self.iters = iters

    @property
    def funcs(self) -> None:
        """
        property representing list of test functions and generators used
        to generate arbitrary values for their parameters.
        """
        funcs = [f for _, f in getmembers(self.module) if isfunction(f)]
        tests = filter(lambda x: self.namePattern.match(str(x)), funcs)
        return tester.validateFuncs(list(map(lambda x:x(), tests)))
    
    def setPattern(self, nameStruct: str) -> None:
        """
        sets the pattern used to identify property test functions. E.g. 
        'prop_' will identify functions which have names such as:
                -   pRoP_test1
                -   Prop_test2
                -   prop_test3
        """
        if type(nameStruct) != str:
            raise TypeError("invalid naming pattern")
        self.namePattern = re.compile(f'^<function {nameStruct}', re.I)

    def setModule(self, module: str) -> None:
        """
        sets the name of the module to identify test functions in.
        """
        try:
            self.module = sys.modules[module]
        except KeyError:
            raise RuntimeError("module not found")
        
    def setIterations(self, iters: int) -> None:
        """
        sets the number of arbitrary values to test each function with. E.g.
        a value of 100 would result in every function being tested for 100
        arbitrary pieces of data.
        """
        if type(iters) != int or iters <= 0:
            raise ValueError("invalid number of iters")
        self.iters = iters

    def runTests(self) -> None:
        """
        Runs the tests with the specified 
        """
        for gens, func in self.funcs:
            tester.runTest(list(map(lambda x: x(), gens)), func, self.iters)
    
    @staticmethod
    def validateFuncs(GFPairs: list) -> list:
        if any([len(x[0]) != len(getfullargspec(x[1])[0]) for x in GFPairs]):
            raise RuntimeError("invalid number of generators provided")
        return GFPairs
    
    @staticmethod
    def runTest(gens: list, func, iters: int) -> None:
        fails = []
        for i in range(iters):
            x = [next(g) for g in gens]
            if not func(*x):
                fails.append(x)
        print(f'\nran {iters} tests, with {len(fails)} failures')
        tester.printFails(fails)

    @staticmethod
    def printFails(fails: list) -> None:
        if len(fails):
            print("These include:")
        for i, val in enumerate(fails):
            if i == 5:
                break
            print(f'\t->\t{val}')

import basicGenerators as bg

def prop_a():
    def new(i):
        print(i)
        return True
    return ([bg.intArb(-100,100)], new)

a = tester(__name__)
a.runTests()