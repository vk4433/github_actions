from src.math import add,sub

def test_add():
    assert add(5, 3) == 8
    assert add (5,2)==6

def test_sub():
    assert sub(5, 3) == 2
    assert sub(5,2)==1