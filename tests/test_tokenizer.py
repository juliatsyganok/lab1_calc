from src.tokens import get_tokens
import pytest

def test_simple_numbers():
    """Тест простых чисел"""
    assert get_tokens("123") == [123]
    assert get_tokens("45.67") == [45.67]

def test_binary_operators():
    """Тест бинарных операторов"""
    assert get_tokens("2 + 3") == [2, '+', 3]
    assert get_tokens("5 - 2") == [5, '-', 2]
    assert get_tokens("3 * 4") == [3, '*', 4]
    assert get_tokens("10 / 2") == [10, '/', 2]
    assert get_tokens("10 // 3") == [10, '//', 3]
    assert get_tokens("7 % 3") == [7, '%', 3]
    assert get_tokens("2 ** 3") == [2, '**', 3]

def test_unary_operators():
    """Тест унарных операторов"""
    assert get_tokens("-5") == [-5]
    assert get_tokens("+3") == [3]
    assert get_tokens("-(2+3)") == ['-', '(', 2, '+', 3, ')']
    assert get_tokens("2 * -3") == [2, '*', -3]

def test_brackets():
    """Тест скобок"""
    assert get_tokens("(2 + 3)") == ['(', 2, '+', 3, ')']
    assert get_tokens("((1 + 2) * 3)") == ['(', '(', 1, '+', 2, ')', '*', 3, ')']

def test_complex_expressions():
    """Тест сложных выражений"""
    assert get_tokens("2 + 3 * 4") == [2, '+', 3, '*', 4]
    assert get_tokens("(2 + 3) * 4") == ['(', 2, '+', 3, ')', '*', 4]
    assert get_tokens("-2 + 3 * -4") == [-2, '+', 3, '*', -4]

def test_spaces_ignored():
    """Тест что пробелы игнорируются"""
    assert get_tokens("2+3") == [2, '+', 3]
    assert get_tokens("  2  +  3  ") == [2, '+', 3]
    assert get_tokens("2\n+\t3") == [2, '+', 3]

def test_error_cases():
    """Тест ошибочных случаев"""
    with pytest.raises(ValueError):
        get_tokens("2 + +") 
    
    with pytest.raises(ValueError):
        get_tokens("2 @ 3") 
    
    with pytest.raises(ValueError):
        get_tokens("12.34.56") 
