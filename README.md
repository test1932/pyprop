## Pyprop - property testing made simple
###### Written by Max Whisson
---

### Usage:
_mytests_ module:

    import pyprop.basicGenerators as bg

    def prop_amazingPropertyTest():
        def func(i, j):
            # assess properties here
            return True # if successful
        return ([bg.intArb(-100, 100), bg.intArb(-100, 100)], func)

_runtests_ module:

    import sys
    import pyprop.testing as pytest
    import basicTests

    testerObj = pytest.testing(basicTests)
    testerObj.runTests()