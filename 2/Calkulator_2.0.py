print("Поддерживаемые операции: +, -, *, /, //, %, ^")
print("Для выхода введите 'q' в качестве операции.\n")

allowed = {"+", "-", "*", "/", "//", "%", "^"}

while True:
    try:
        # первое число
        raw = input("Введите первое число (или 'q' для выхода): ").strip().replace(",", ".")
        if raw.lower() == "q":
            print("Выход из программы.")
            break
        try:
            a = float(raw)
        except ValueError:
            print("Ошибка: введено не число. Попробуйте ещё раз.\n")
            continue

        # операция 
        op = input("Введите операцию (+, -, *, /, //, %, ^): ").strip()
        if op.lower() == "q":
            print("Выход из программы.")
            break
        if op not in allowed:
            print("Ошибка: неизвестная операция. Допустимые: +, -, *, /, //, %, ^\n")
            continue

        # второе число
        raw = input("Введите второе число: ").strip().replace(",", ".")
        try:
            b = float(raw)
        except ValueError:
            print("Ошибка: введено не число. Попробуйте ещё раз.\n")
            continue

        # вычисление
        if op in ("/", "//", "%") and b == 0:
            print("Ошибка: Деление на ноль невозможно.\n")
            continue

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = a / b
        elif op == "//":
            result = a // b
        elif op == "%":
            result = a % b
        elif op == "^":
            result = a ** b

        # форматирование результата 
        if isinstance(result, float) and result.is_integer():
            result_str = str(int(result))
        else:
            result_str = str(result)

        print(f"Результат: {result_str}\n")

        # вопрос о продолжении работы
        while True:
            answer = input("Хотите выполнить ещё одну операцию? (да/нет): ").strip().lower()
            if answer == "да":
                print()
                break
            elif answer == "нет":
                print("Работа программы завершена.")
                raise SystemExit
            else:
                print("Ошибка: введите 'да' или 'нет'.")

    except (KeyboardInterrupt, EOFError):
        print("\nПрерывание. Выход из программы.")
        break