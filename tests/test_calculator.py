from src.calculator import add, divide, percentage


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_percentage():
    assert percentage(200, 10) == 20
    assert percentage(50, 50) == 25.0
    assert percentage(100, -10) == -10.0
    assert percentage(0, 100) == 0.0
