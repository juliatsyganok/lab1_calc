from tokens import get_tokens
from expr import expr_

def calculate(expression: str) -> int|float:
    """
    Главная функция 
    """
    tokens = get_tokens(expression)
    result, final_index = expr_(tokens, 0)
    return result
