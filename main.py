def pyramid_number(n: int) -> int:
    if n <= 0:
        raise ValueError("n має бути додатним числом.")
    Pn = 0
    for k in range(1, n + 1):
        Pn += k * (k + 1) // 2
    return Pn

def menu():
    while True:
        print("\nМеню:")
        print("1. Обчислити n-те пірамідальне число")
        print("2. Вийти з програми")
        choice = input("Введіть номер дії: ")
        if choice == "1":
            try:
                n = int(input("Введіть номер елемента n: "))
                result = pyramid_number(n)
                print(f"{n}-те пірамідальне число: {result}")
            except ValueError as e:
                print(f"Помилка: {e}")
        elif choice == "2":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
            
#menu()