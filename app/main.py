def add(a: float, b: float) -> float:
    return a + b


def main():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        result = add(a, b)
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введите числа")


if __name__ == "__main__":
    main()