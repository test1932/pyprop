# Pyprop - property based testing made simple (maybe)
## Overview:
This package was created to allow Python users to utilise property based testing in a similar manner to Haskell's _QuickCheck_ package.

Property based testing allows for a more complete 'proving' of a program's correctness by ensuring the overall behaviour of functions is correct. This is in contrast to testing individual test cases - a unit testing approach. Property based testing is, however, not particularly well suited to testing very stateful programs.

## Thinking _Correctly_:
E.g. Testing that a sorting function works as intended.

In this case, to ensure that the function _mysort_ is behaving correctly, we may want to test that is has the following properties:

- the items in the resulting list are in sorted order (kind of obvious - we want the sorting algorithm to sort things)
- every unique value from the input list appears in the output list the same number of times (no values are disappearing/being duplicated)
- the resulting list has the same number of items as the original list (ensure that new items aren't introduced)

If these _properties_ hold, it can be concluded that the sorting algorithm is performing correctly.

## Usage:
The following is an implementation of some tests for ensuring that a sorting function _mysort_ works correctly. The methodology follows that described in the previous section:

_mytests_ module:

    import pyprop.basicGenerators as bg

    def prop_amazingPropertyTest():
        def func(i, j):
            # assess properties here
            return True # if successful
        return ([bg.intArb(-100, 100), bg.intArb(-100, 100)], func)

_runtests_ module:

    import pyprop.testing as pytest
    import mytests

    # 1000 iterations per function, dumps results to 'myfile.txt'
    testerObj = pytest.testing('mytests', iters = 1000, f = 'myfile.txt')
    testerObj.runTests()