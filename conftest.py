import pytest


@pytest.fixture()
def separator():
    yield 'value'

@pytest.fixture(scope='session')
def all_tests():
    print('before all')
    yield
    print('after all')