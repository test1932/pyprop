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
The general structure of a test within a class is as follows:

    @staticmethod
    def prop_equalLength():
        def test(i):
            return len(i) == len(sorted(i))
        return ([bg.intListArb(10)], test)

- _prop_equalLength_ is the function for producing the test with generators
- _test_ is the test to be run
- _[bg.intListArb(10)]_ is the list of generators used to produce the test function's inputs (i)

The following is an implementation of some tests for ensuring that the sorting function _sorted_ works correctly. The methodology follows that described in the previous section:

    import pyprop.basicGenerators as bg
    import pyprop.testing as pytest

    class sortingTests:
        @staticmethod
        def prop_equalLength():
            def test(i):
                return len(i) == len(sorted(i))
            return ([bg.intListArb(10,-100,100)], test)

        @staticmethod
        def prop_sortedResult():
            def test(i):
                res = sorted(i)
                return all([res[i] <= res[i + 1] for i in range(len(res) - 1)])
            return ([bg.intListArb(10,-100,100)], test)
        
        @staticmethod
        def prop_containsSameElements():
            def test(i):
                res = sorted(i)
                ifreq = {x:i.count(x) for x in i}
                return ifreq == {x:res.count(x) for x in res}
            return ([bg.intListArb(10,-100,100)], test)


    testerObj = pytest.tester(classes = [sortingTests])
    testerObj.runTests()

This produces output:

    testing sortingTests:
	testing prop_containsSameElements:		ran 100 test(s), with 0 failure(s)
	testing prop_equalLength:		ran 100 test(s), with 0 failure(s)
	testing prop_sortedResult:		ran 100 test(s), with 0 failure(s)
    ==================================================
    0 test(s) failed (100.0%):
    ==================================================

Signifying that all of the tests passed, and the _sorted()_ function has all of the properties which we want it to have.