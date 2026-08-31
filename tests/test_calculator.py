from src.calculator import add, divide, percentage


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5

def test_percentage():
    assert percentage(200, 10) == 20
