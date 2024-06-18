from pdmdemo.main import simplesum


def test_simplesum():
    assert simplesum([1, 2, 3]) == 6
    assert simplesum([]) == 0
