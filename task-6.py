items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    """Жадібний алгоритм для вибору страв з максимальним співвідношенням калорій/вартість."""
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            chosen_items.append(name)
            total_calories += info['calories']
            total_cost += info['cost']

    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    """Алгоритм динамічного програмування для оптимального вибору страв."""
    item_names = list(items.keys())
    n = len(item_names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Побудова таблиці dp
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]['cost']
        calories = items[name]['calories']

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлення обраних страв
    chosen_items = []
    total_calories = dp[n][budget]
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = item_names[i - 1]
            chosen_items.append(name)
            b -= items[name]['cost']

    chosen_items.reverse()  # Оскільки ми збирали страви у зворотному порядку

    return chosen_items, total_calories, budget - b


# Приклад використання
budget = 100

print("Жадібний алгоритм:")
greedy_result = greedy_algorithm(items, budget)
print(f"Обрані страви: {greedy_result[0]}, Калорії: {greedy_result[1]}, Витрачено: {greedy_result[2]}")

print("\nДинамічне програмування:")
dp_result = dynamic_programming(items, budget)
print(f"Обрані страви: {dp_result[0]}, Калорії: {dp_result[1]}, Залишок бюджету: {dp_result[2]}")
