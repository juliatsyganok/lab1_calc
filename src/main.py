from calc import calculate
from tokens import get_tokens

def main() -> None:
    """
    Главная функция - точка входа в калькулятор.

    Пользовательский ввод обрабатывается до команды stop

    Returns:
        None: не возвращает значение, только счиатет результат выражения
    """
    while True:
        print("Начало работы. Введите выражение или 'stop' для выхода")
        case = input()
        case = str(case)

        if case.lower() == 'stop':
            break
        if not case:
            continue

        try:
            tokens = get_tokens(case)
            result = calculate(tokens)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()