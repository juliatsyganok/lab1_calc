OPERATORS = {'+', '-', '*', '/', '//', '%', '**'}
FIRST_PRI = {'*', '/', '//', '%', '**'}
SECOND_PRI = {'+', '-'} 
BRACKETS = {'(', ')'}


def get_tokens(case: str) -> list[int | float | str]:
    """
    Разбирает входное выражение на токены, причем унарный знак является частью токена

    Args:
        case: входная строка с выражением
    Returns:
        tokens: список токенов (int, float, str)
    """
    case = ''.join(str(i) for i in case)
        
    tokens = []
    i = 0

    while i < len(case):
        if case[i].isspace():
            i += 1
            continue

        elif case[i] in SECOND_PRI:
            if i == 0 or (tokens and (tokens[-1] in OPERATORS or tokens[-1] == '(')):
                sign = case[i]
                i += 1
                while i < len(case) and case[i].isspace():
                    i += 1
                if i >= len(case):
                    raise ValueError("После унарного знака ожидалось число или скобка")
                if case[i] == '(':
                    tokens.append(sign)
                    continue
                elif case[i].isdigit() or case[i] == '.':
                    start = i
                    has_dot = False
                    while i < len(case) and (case[i].isdigit() or case[i] == '.'):
                        if case[i] == '.':
                            has_dot = True
                        i += 1

                    if i > start:
                        number_str = sign + case[start:i]
                        try:
                            if has_dot:
                                tokens.append(float(number_str))
                            else:
                                tokens.append(int(number_str))
                        except ValueError:
                            raise ValueError(f"Неправильное число: '{number_str}'")
                    else:
                        raise ValueError("После унарного знака ожидалось число")
                    continue
                else:
                    raise ValueError("После унарного знака ожидалось число или скобка")
            else:
                tokens.append(case[i])
                i += 1

        elif case[i] in FIRST_PRI:
            if i + 1 < len(case) and case[i:i+2] in ('//', '**'):
                tokens.append(case[i:i+2])
                i += 2
            else:
                tokens.append(case[i])
                i += 1
        elif case[i] in BRACKETS:
            tokens.append(case[i])
            i += 1
        elif case[i].isdigit() or case[i] == '.':
            start = i
            has_dot = False
            while i < len(case) and (case[i].isdigit() or case[i] == '.'):
                if case[i] == '.':
                    has_dot = True
                i += 1

            try:
                if has_dot:
                    tokens.append(float(case[start:i]))
                else:
                    tokens.append(int(case[start:i]))
            except ValueError:
                raise ValueError(f"Неправильное число: '{case[start:i]}'")

        else:
            raise ValueError(f"Неизвестный символ: '{case[i]}'")

    return tokens
