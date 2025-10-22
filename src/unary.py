def unary(tokens: list[int | float | str], index: int) -> tuple:
    """
    Обрабатывает унарные + и -
    
    Args:
    tokens: токены полученные из выражения функцией get_tokens
    index: индекс текущего токена

    """
    if index >= len(tokens):
        raise SyntaxError("Конец выражения")
    
    token = tokens[index]
    
    if token in ('+', '-'):
        value, new_index = unary(tokens, index + 1)
        
        if token == '-':
            return -value, new_index
        else:
            return value, new_index
    else:
        from primary import primary_
        return primary_(tokens, index)