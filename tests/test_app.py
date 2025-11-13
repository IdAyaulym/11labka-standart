from src import app

def test_is_palindrome_true():
    assert app.is_palindrome("A man, a plan, a canal: Panama") is True

def test_is_palindrome_false():
    assert app.is_palindrome("hello") is False

def test_sum_numbers():
    assert app.sum_numbers([1,2,3,4]) == 10
