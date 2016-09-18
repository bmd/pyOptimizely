import context
from optimizely import Optimizely

def test_instantiates_optimizely():
    assert True


def test_expected_base_attributes():
    token = 'abc123'
    opt = Optimizely(token)

