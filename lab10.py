import numpy as np
import random

N = 15
distanceMatrix = np.array([
    [0.00, 13.60, 13.34, 10.63, 5.83, 14.00, 12.21, 4.12, 10.82, 9.22, 3.16, 12.53, 4.47, 8.60, 11.40],
    [13.60, 0.00, 7.00, 5.83, 13.45, 4.12, 4.24, 12.00, 10.77, 7.62, 13.89, 2.83, 13.60, 8.54, 5.00],
    [13.34, 7.00, 0.00, 11.18, 10.20, 3.16, 10.44, 13.89, 5.00, 12.21, 12.00, 9.22, 11.05, 12.81, 10.77],
    [10.63, 5.83, 11.18, 0.00, 13.00, 9.22, 2.00, 7.62, 13.04, 2.00, 12.21, 3.16, 12.53, 3.00, 1.00],
    [5.83, 13.45, 10.20, 13.00, 0.00, 12.08, 13.89, 9.22, 6.08, 12.37, 2.83, 13.60, 1.41, 12.17, 13.42],
    [14.00, 4.12, 3.16, 9.22, 12.08, 0.00, 8.06, 13.60, 7.81, 10.63, 13.34, 6.71, 12.65, 11.40, 8.60],
    [12.21, 4.24, 10.44, 2.00, 13.89, 8.06, 0.00, 9.49, 13.04, 4.00, 13.45, 1.41, 13.60, 5.00, 1.00],
    [4.12, 12.00, 13.89, 7.62, 9.22, 13.60, 9.49, 0.00, 12.81, 5.83, 7.00, 10.20, 8.06, 5.00, 8.54],
    [10.82, 10.77, 5.00, 13.04, 6.08, 7.81, 13.04, 12.81, 0.00, 13.34, 8.54, 12.17, 7.28, 13.60, 13.00],
    [9.22, 7.62, 12.21, 2.00, 12.37, 10.63, 4.00, 5.83, 13.34, 0.00, 11.18, 5.10, 11.70, 1.00, 3.00],
    [3.16, 13.89, 12.00, 12.21, 2.83, 13.34, 13.45, 7.00, 8.54, 11.18, 0.00, 13.45, 1.41, 10.77, 12.81],
    [12.53, 2.83, 9.22, 3.16, 13.60, 6.71, 1.41, 10.20, 12.17, 5.10, 13.45, 0.00, 13.45, 6.08, 2.24],
    [4.47, 13.60, 11.05, 12.53, 1.41, 12.65, 13.60, 8.06, 7.28, 11.70, 1.41, 13.45, 0.00, 11.40, 13.04],
    [8.60, 8.54, 12.81, 3.00, 12.17, 11.40, 5.00, 5.00, 13.60, 1.00, 10.77, 6.08, 11.40, 0.00, 4.00],
    [11.40, 5.00, 10.77, 1.00, 13.42, 8.60, 1.00, 8.54, 13.00, 3.00, 12.81, 2.24, 13.04, 4.00, 0.00]
])

def unitInitialization():
    '''
    Генерирует особь и возвращает её
    '''
    unit = list(range(N))
    random.shuffle(unit)
    return unit

def greedyMethod():
    '''
    Метод жадного алгоритма. Строит маршрут 
    '''
    solution = [0] * N 
    visited = [False] * N 
    solution[0] = random.randint(0, N-1) 
    visited[solution[0]] = True 

    for i in range(1, N): 
        currentСity = solution[i - 1] 
        min = float('inf')  
        nextСity = -1 

        for j in range(N):
            if not visited[j] and distanceMatrix[currentСity][j] < min: 
                min = distanceMatrix[currentСity][j] 
                nextСity = j 

        solution[i] = nextСity 
        visited[nextСity] = True 

    return solution

def calcFitness(solution):
    '''
    Функция для подсчета приспособлености (общего расстояния между всеми городами особи)
    '''
    fitness = 0
    for i in range(N - 1):
        A, B = solution[i], solution[i + 1]
        fitness += distanceMatrix[A][B]
    C, D = solution[N - 1], solution[0]
    fitness += distanceMatrix[C][D]
    return fitness

def crossoverOX(parent1, parent2):
    '''
    Функция скрещивания двух особей для получения "потомства"
    '''
    start = random.randint(0, N-1)
    end = random.randint(0, N-1)
    if start > end:
        start, end = end, start

    child = [-1] * N

    for i in range(start, end + 1):
        if parent1[i] not in child:
            child[i] = parent1[i]

    index = 0

    for i in range(N):
        if index == start:
            index = end + 1

        if parent2[i] not in child:
            child[index] = parent2[i]
            index += 1
    return child

def mutate(child):
    '''
    Функция мутации "потомства" после скрещивания
    '''
    mutationRate = 0.89 # шанс мутации
    for i in range(N):
        if random.random() < mutationRate:
            a = i
            b = random.randint(0, N-1)
            child[a], child[b] = child[b], child[a]
    return child

def printMatrix(matrix):
    """
    Вывод матрицы
    """
    maxElementLength = max(len(str(element)) for row in matrix for element in row)
    cols = len(matrix[0])
    topBorder = " " + "-" * ((maxElementLength + 1) * cols + 1)
    print ("Заданная матрица: ")
    print (topBorder)
    for row in matrix:
        print("|", end="")
        for element in row:
            if element == row[len(row) - 1]:
                print(f" {element:{maxElementLength}}", end="|")
            else:
                print(f" {element:{maxElementLength}}", end="")
        print() 

        print("|", end="")
        print("-" * ((maxElementLength + 1) * cols + 1))

def main():

    populationsNumber = int(input("Введите размер популяции: "))
    generations = int(input("Введите количество поколений: "))

    print("\tДоступные операторы начальной полпуляции:")
    print("1 - Формирование популяции Жадным Алгоритмом")
    print("2 - Случайное формирование популяции")
    print("3 - Смешанное формирование популяции")

    modeInit = int(input("Выберите оператор формирования начальной популяции (1-3): "))
    if modeInit not in range(1,4):
        raise Exception("Выбран некорректный оператор")

    population = [0] * populationsNumber

    printMatrix(distanceMatrix)

    for i in range(populationsNumber):
        if modeInit == 1:
            population[i] = greedyMethod()  
        elif modeInit == 2:
            population[i] = unitInitialization()
        elif modeInit == 3:
            bestRate = 0.3
            if random.random() < bestRate:
                population[i] = greedyMethod()
            else:
                population[i] = unitInitialization()
    generation = 0

    fitness = [calcFitness(ind) for ind in population]

    while generation < generations:
        print(f"\nПоколение № {generation + 1}:")
        for i in range(populationsNumber):
            print(" ".join(str(ind + 1) for ind in population[i]), f"{population[i][0] + 1} | Приспособленность особи: {fitness[i]}")

        index = np.argmin(fitness)
        print("Лучшая особь:", " ".join(str(ind + 1) for ind in population[index]), f"{population[index][0] + 1} | Приспособленность: {fitness[index]}", end="\n")

        for i in range(populationsNumber):
            ind1, ind2 = [random.randint(0, populationsNumber - 1) for _ in range(2)]
            parents = population[ind1], population[ind2]
            crossoverRate = 0.95 # шанс скрещивания
            if random.random() < crossoverRate:
                child = crossoverOX(parents[0], parents[1])
                child = mutate(child)
                childFitness = calcFitness(child)

                if childFitness < calcFitness(population[ind1]):
                    population[ind1] = child
                elif childFitness < calcFitness(population[ind2]):
                    population[ind2] = child

                fitness = [calcFitness(ind) for ind in population]

        generation += 1

    index = np.argmin(fitness)
    print("\nЛучшее найденное решение:", " ".join(str(ind + 1) for ind in population[index]), f"{population[index][0] + 1}")
    print("Приспособленность лучшей особи:", fitness[index])

if __name__ == "__main__":
    main()
