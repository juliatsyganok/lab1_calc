def add(tokens: list[int | float | str], index: int) -> tuple:
    """
    Обрабатывает + и -

    Args:
    tokens: токены полученные из выражения функцией get_tokens
    index: индекс текущего токена

    """
    from mul import mul
    result, new_index = mul(tokens, index)

    while new_index < len(tokens) and tokens[new_index] in ('+', '-'):
        op = tokens[new_index]
        new_index += 1
        
        right_value, next_index = mul(tokens, new_index)
        
        if op == '+':
            result += right_value
        elif op == '-':
            result -= right_value
        
        new_index = next_index
    
    return result, new_index