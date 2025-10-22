def primary_(tokens: list[int | float | str], index: int) -> tuple:
    """ 
    Обрабатывает числа и скобки

    Args:
        tokens: токены полученные из выражения функцией get_tokens
        index: индекс текущего токена
    """ 
    if index >= len(tokens):
        raise SyntaxError("Конец выражения")

    token = tokens[index]

    if isinstance(token, (int, float)):
        return token, index + 1
    
    elif token == '(':
        from expr import expr_
        result, new_index = expr_(tokens, index + 1)
        if new_index >= len(tokens) or tokens[new_index] != ')':
            raise SyntaxError("Ожидалась закрывающая скобка ')'")
        
        return result, new_index + 1

    else:
        raise SyntaxError(f"Ожидалось число или '(', получено: {token}")