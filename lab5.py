import random
import math

# матрица расстояний
distance_matrix = [
        [0, 2, 3, 4, 5],
        [2, 0, 6, 7, 8],
        [3, 6, 0, 9, 10],
        [4, 7, 9, 0, 11],
        [5, 8, 10, 11, 0]
    ]

# Функция для вычисления общей длины пути
def total_distance(path, distance_matrix):
    total = 0
    for i in range(len(path) - 1):
        total += distance_matrix[path[i]][path[i+1]]
    total += distance_matrix[path[-1]][path[0]]  # Расстояние от последнего к первому городу
    return total

# Алгоритм коммивояжера
def solve_TSP(distance_matrix):
    N = len(distance_matrix)
    X = list(range(N))
    print("X: ", X)
    random.shuffle(X)
    S = [0] * N
    print("S: ", S)
    i = 0
    S[i] = X.pop(0)
    print("X2: ", X)
    print("S2: ", S)
    i += 1

    while len(X) > 0:
        min_distance = float('inf')
        for x_j in X:
            dist = distance_matrix[S[i - 1]][x_j]
            if dist < min_distance:
                min_distance = dist
                S[i] = x_j
        X.remove(S[i])
        i += 1

    # Вычисляем общую длину пути
    total_dist = total_distance(S, distance_matrix)
    return S, total_dist

# Пример использования
if __name__ == "__main__":

    # Вывод матрицы расстояний
    print("Distance Matrix:")
    for row in distance_matrix:
        print(row)

    # Решение задачи коммивояжера
    solution_path, total_length = solve_TSP(distance_matrix)
    print(f"\nOptimal path: {solution_path}")
    print(f"Total distance: {total_length}")
