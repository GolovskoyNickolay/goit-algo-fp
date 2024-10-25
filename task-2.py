import turtle
import math


# Функція для малювання фрактального "дерева Піфагора"
def draw_pythagoras_tree(branch_length, level, angle):
    if level == 0:
        return

    # Малюємо стовбур
    turtle.forward(branch_length)

    # Ліва гілка
    turtle.left(angle)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1, angle)

    # Повертаємося до початкової позиції для правої гілки
    turtle.right(2 * angle)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1, angle)

    # Повертаємося назад у початкову точку
    turtle.left(angle)
    turtle.backward(branch_length)


# Основна програма для налаштування користувача
def main():
    # Налаштування Turtle
    turtle.speed(0)  # Максимальна швидкість малювання
    turtle.left(90)  # Початкова орієнтація "черепашки"
    turtle.up()
    turtle.goto(0, -300)  # Початкова позиція (корінь дерева)
    turtle.down()

    # Запит у користувача на глибину рекурсії
    level = int(input("Введіть рівень рекурсії для дерева Піфагора (рекомендується 5-10): "))
    initial_branch_length = 150  # Довжина першої гілки
    angle = 45  # Кут відхилення

    # Малювання дерева
    draw_pythagoras_tree(initial_branch_length, level, angle)

    # Завершення роботи Turtle
    turtle.done()


# Виклик основної програми
if __name__ == "__main__":
    main()
