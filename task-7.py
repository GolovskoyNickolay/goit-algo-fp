import random
import matplotlib.pyplot as plt
import numpy as np


def monte_carlo_simulation(num_rolls=100000):
    sums = {i: 0 for i in range(2, 13)}  # Ініціалізуємо кількість для всіх можливих сум від 2 до 12

    # Імітуємо кидки двох кубиків
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        sums[total] += 1

    # Обчислюємо ймовірності кожної суми
    probabilities = {key: (value / num_rolls) * 100 for key, value in sums.items()}

    return sums, probabilities


def plot_probabilities(probabilities):
    # Побудова графіка ймовірностей
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, color='skyblue', edgecolor='black')
    plt.xticks(sums)
    plt.xlabel("Сума на двох кубиках")
    plt.ylabel("Ймовірність (%)")
    plt.title("Ймовірності сум методом Монте-Карло")
    plt.show()


# Виконання симуляції
num_rolls = 100000
sums, probabilities = monte_carlo_simulation(num_rolls)

# Вивід результатів
print("Результати симуляції Монте-Карло:")
for total, prob in probabilities.items():
    print(f"Сума: {total}, Ймовірність: {prob:.2f}%")

# Побудова графіка ймовірностей
plot_probabilities(probabilities)

# Аналітичні ймовірності для порівняння
analytical_probs = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Порівняння результатів
print("\nПорівняння аналітичних та отриманих ймовірностей:")
for total in range(2, 13):
    sim_prob = probabilities[total]
    ana_prob = analytical_probs[total]
    print(f"Сума: {total}, Монте-Карло: {sim_prob:.2f}%, Аналітична: {ana_prob:.2f}%")
