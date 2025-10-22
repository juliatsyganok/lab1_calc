def pow_(tokens: list[int | float | str], index: int) -> tuple:
    """
    Обрабатывает **
    
    Args:
    tokens: токены полученные из выражения функцией get_tokens
    index: индекс текущего токена

    """
    from unary import unary
    left_value, new_index = unary(tokens, index)
    
    if new_index < len(tokens) and tokens[new_index] == '**':
        right_value, next_index = pow_(tokens, new_index + 1)
        return left_value ** right_value, next_index
    else:
        return left_value, new_index