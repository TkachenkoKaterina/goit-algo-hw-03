import turtle


def draw_koch_segment(t, length, level):
    """
    Функція для малювання одного сегменту сніжинки Коха
    :param t: об'єкт черепашки
    :param length: довжина лінії
    :param level: рівень рекурсії
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)
        t.right(120)
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)


def draw_koch_snowflake(t, length, level):
    """
    Функція для малювання сніжинки Коха
    :param t: об'єкт черепашки
    :param length: довжина сторони сніжинки
    :param level: рівень рекурсії
    """
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)


def main():
    level = int(input("Вкажіть рівень рекурсії (0 або більше): "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    draw_koch_snowflake(t, 400, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
