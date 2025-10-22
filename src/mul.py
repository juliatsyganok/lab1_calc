def mul(tokens: list[int | float | str], index: int) -> tuple:
    """
    Обрабатывает *, /, //, %
    
    Args:
    tokens: токены полученные из выражения функцией get_tokens
    index: индекс текущего токена

    """
    from pow import pow_
    result, new_index = pow_(tokens, index)
    
    while new_index < len(tokens) and tokens[new_index] in ('*', '/', '//', '%'):
        op = tokens[new_index]
        new_index += 1
        
        right_value, next_index = pow_(tokens, new_index)
        
        if op == '*':
            result *= right_value
        elif op == '/':
            if right_value == 0:
                raise ZeroDivisionError("Деление на ноль")
            result /= right_value
        elif op == '//':
            if not isinstance(result, int) or not isinstance(right_value, int):
                raise ValueError("Оператор '//' можно применять только к целым числам")
            if right_value == 0:
                raise ZeroDivisionError("Деление на ноль")
            result //= right_value
        elif op == '%':
            if not isinstance(result, int) or not isinstance(right_value, int):
                raise ValueError("Оператор '%' можно применять только к целым числам")
            if right_value == 0:
                raise ZeroDivisionError("Деление на ноль")
            result %= right_value
        
        new_index = next_index
    
    return result, new_index