def hanoi(n, source, target, auxiliary, state):
    if n == 1:
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
    else:
        hanoi(n - 1, source, auxiliary, target, state)
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        hanoi(n - 1, auxiliary, target, source, state)


def main():
    n = int(input("Введіть кількість дисків: "))

    state = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }

    print(f"Початковий стан: {state}")

    hanoi(n, 'A', 'C', 'B', state)

    print(f"Кінцевий стан: {state}")


if __name__ == "__main__":
    main()
