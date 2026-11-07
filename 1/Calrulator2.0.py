def get_number(prompt: str) -> float:
    """Запрашивает у пользователя число с проверкой корректности."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Ошибка: введено не число. Попробуйте ещё раз.")


def get_operation() -> str:
    """Запрашивает у пользователя математическую операцию."""
    allowed = {"+", "-", "*", "/", "//", "%", "^"}
    while True:
        op = input("Введите операцию (+, -, *, /, //, %, ^): ").strip()
        if op in allowed:
            return op
        print("Ошибка: неизвестная операция. Допустимые: +, -, *, /, //, %, ^")


def calculate(a: float, op: str, b: float) -> float:
    """Выполняет арифметическую операцию.

    Возвращает результат или выбрасывает ValueError при делении на ноль.
    """
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a / b
    if op == "//":
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a // b
    if op == "%":
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a % b
    if op == "^":
        return a ** b
    raise ValueError(f"Неизвестная операция: {op}")


def format_result(value: float) -> str:
    """Красиво форматирует результат (убирает .0 у целых чисел)."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def ask_continue() -> bool:
    """Спрашивает, хочет ли пользователь выполнить ещё одну операцию.

    Возвращает True, если пользователь ответил 'да',
    False — если 'нет'. При некорректном ответе переспрашивает.
    """
    while True:
        answer = input("Хотите выполнить ещё одну операцию? (да/нет): ").strip().lower()
        if answer in {"да", "д", "yes", "y"}:
            return True
        if answer in {"нет", "н", "no", "n"}:
            return False
        print("Ошибка: введите 'да' или 'нет'.")


def main() -> None:
    print("Поддерживаемые операции: +, -, *, /, //, %, ^")
    print("Для выхода введите 'q' в качестве первого числа.\n")

    while True:
        try:
            first_raw = input("Введите первое число (или 'q' для выхода): ").strip()
            if first_raw.lower() == "q":
                print("Выход из программы.")
                break

            try:
                a = float(first_raw.replace(",", "."))
            except ValueError:
                print("Ошибка: введено не число. Попробуйте ещё раз.\n")
                continue

            op_input = input("Введите операцию (+, -, *, /, //, %, ^): ").strip()
            if op_input.lower() == "q":
                print("Выход из программы.")
                break

            allowed = {"+", "-", "*", "/", "//", "%", "^"}
            if op_input not in allowed:
                print("Ошибка: неизвестная операция. Допустимые: +, -, *, /, //, %, ^\n")
                continue

            b = get_number("Введите второе число: ")

            try:
                result = calculate(a, op_input, b)
            except ValueError as err:
                print(f"Ошибка: {err}\n")
                continue

            print(f"Результат: {format_result(result)}\n")

            if not ask_continue():
                print("Работа программы завершена.")
                break

        except (KeyboardInterrupt, EOFError):
            print("\nПрерывание. Выход из программы.")
            break


if __name__ == "__main__":
    main()