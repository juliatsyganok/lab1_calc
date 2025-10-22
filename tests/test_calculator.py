from src.calc import calculate
import pytest

def test_basic_operations():
    """Тест базовых операций"""
    assert calculate("2 + 3") == 5
    assert calculate("5 - 2") == 3
    assert calculate("3 * 4") == 12
    assert calculate("10 / 2") == 5.0
    assert calculate("2 ** 3") == 8

def test_priority():
    """Тест приоритета операций"""
    assert calculate("2 + 3 * 4") == 14
    assert calculate("(2 + 3) * 4") == 20
    assert calculate("2 * 3 + 4") == 10
    assert calculate("2 + 3 * 4 - 1") == 13

def test_unary_operations():
    """Тест унарных операций"""
    assert calculate("-5") == -5
    assert calculate("+3") == 3
    assert calculate("-(2+3)") == -5
    assert calculate("2 * -3") == -6
    assert calculate("-2 + 5") == 3

def test_power_priority():
    """Тест приоритета степени"""
    assert calculate("2 ** 3 ** 2") == 512  # 2^(3^2) = 2^9
    assert calculate("(2 ** 3) ** 2") == 64  # (2^3)^2 = 8^2

def test_integer_operations():
    """Тест целочисленных операций"""
    assert calculate("10 // 3") == 3
    assert calculate("7 % 3") == 1
    assert calculate("10 // 3 + 5 % 2") == 4

def test_complex_expressions():
    """Тест сложных выражений"""
    assert calculate("2 + 3 * (4 - 1)") == 11
    assert calculate("(1 + 2) * (3 + 4)") == 21
    assert calculate("- (3 + 2) * -4") == 20
    assert calculate("2 ** 3 * 4") == 32

def test_float_operations():
    """Тест операций с дробями"""
    assert calculate("5.5 + 2.5") == 8.0
    assert calculate("3.0 * 2.5") == 7.5
    assert calculate("10.0 / 4") == 2.5

def test_error_cases():
    """Тест ошибочных случаев"""
    with pytest.raises(ZeroDivisionError):
        calculate("5 / 0")
    
    with pytest.raises(ZeroDivisionError):
        calculate("5 // 0")
    
    with pytest.raises(ValueError):
        calculate("5.5 // 2") 
    
    with pytest.raises(SyntaxError):
        calculate("2 + + 3")  
    
    with pytest.raises(SyntaxError):
        calculate("(2 + 3") 
