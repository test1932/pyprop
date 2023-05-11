from inspect import getmembers, isfunction, getfullargspec
import sys
import re

class tester:
    """
    class for creating testing objects to test modules.
    """
    def __init__(self, module, n = "prop_", iters = 100, f = None) -> None:
        """
        constructor method.
        """
        self.setModule(module)
        self.setPattern(n)
        self.setIterations(iters)
        self.dumpFile = f

    @property
    def __funcs(self) -> None:
        """
        property representing list of test functions and generators used
        to generate arbitrary values for their parameters.
        """
        funcs = [(f, f.__name__) for _, f in getmembers(self.__module) 
                    if isfunction(f)]
        ts = filter(lambda x: self.__namePattern.match(x[1]), funcs)
        return tester.__validateFuncs(list(map(lambda x:(x[0](),x[1]), ts)))
    
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
        self.__namePattern = re.compile(f'^{nameStruct}', re.I)

    def setModule(self, module: str) -> None:
        """
        sets the name of the module to identify test functions in.
        """
        try:
            self.__module = sys.modules[module]
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
        self.__iters = iters

    def runTests(self) -> None:
        """
        Runs the tests in the specified module with the specified naming.
        """
        fails = []
        fileObj = open(self.dumpFile, "w") if self.dumpFile else None
        for (gens, func), fname in self.__funcs:
            print(f'testing {fname}:\t\t', end = "")
            generators = list(map(lambda x: x(), gens))
            if not tester.__run(generators, func, self.__iters):
                fails.append(fname)
        self.__produceReport(fileObj, fails)

    def __produceReport(self, dumpfile, fails):
        """
        produces final report of the results of testing
        """
        print('=' * 50)
        print(f'{len(fails)} test(s) failed:')
        for tname in fails:
            print(f'\t * {tname}')
        print('=' * 50)
        self.dumpToFile(fails, dumpfile)

    def dumpToFile(self, fails, dumpfile):
        """
        writes testing report to file if a descriptor exists.
        """
        if dumpfile:
            dumpfile.write('=' * 50 + "\n")
            dumpfile.write(f'{len(fails)} test(s) failed:\n')
            for tname in fails:
                dumpfile.write(f'\t * {tname}\n')
            dumpfile.write('=' * 50 + "\n")
            dumpfile.close()

    @staticmethod
    def __validateFuncs(fs: list) -> list:
        """
        validates whether the number of generators provided is correct for
        each function.
        """
        if any([len(x[0][0]) != len(getfullargspec(x[0][1])[0]) for x in fs]):
            raise RuntimeError("invalid number of generators provided")
        return fs
    
    @staticmethod
    def __run(gens: list, func, iters: int) -> bool:
        """
        runs specified function using generators and reports inaccuracies.
        """
        fails = []
        for i in range(iters):
            x = [next(g) for g in gens]
            try:
                if not func(*x):
                    fails.append(x)
            except:
                fails.append(x)
        print(f'ran {iters} test(s), with {len(fails)} failure(s)')
        tester.__printFails(fails)
        return len(fails) == 0

    @staticmethod
    def __printFails(fails: list) -> None:
        """
        prints out the values which caused errors (if any).
        """
        if len(fails):
            print("These include:")
        for i, val in enumerate(fails):
            if i == 5:
                break
            print(f'\t->\t{val}')