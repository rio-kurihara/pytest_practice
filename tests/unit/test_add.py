from src.app import add

def test_add():
    a = 1
    b = 1
    ans = add(a, b)
    expected = 2

    assert ans == expected

