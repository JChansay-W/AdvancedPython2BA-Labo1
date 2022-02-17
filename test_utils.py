import pytest
import utils

def test_fact():
    with pytest.raises(ValueError):
        utils.fact(-2)
    assert utils.fact(0) == 1
    assert utils.fact(4) == 24
    assert utils.fact(5) == 120

def test_roots():
    # À compléter...
    pass

def test_integrate():
    # À compléter...
    pass
