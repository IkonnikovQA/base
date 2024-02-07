import pytest

@pytest.mark.regres
def test_one_is_one(separator, all_tests):
    assert 1 == 1

@pytest.mark.smoke
def test_two_is_two():
    assert 2 == 2

@pytest.mark.skip('Bug')
def test_three_is_three():
    assert 3 == 2