import pyproptest.basicGenerators as bg
import pyproptest.testing as pytest

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