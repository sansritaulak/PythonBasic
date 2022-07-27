import testing
 
def test_calc_sum():
    total = testing.calc_sum(1,2)
    assert total == 3

def test_calc_multiply():
    r = testing.calc_multiply(2,10)
    assert r == 20