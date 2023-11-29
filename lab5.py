import random

distanceMatrix = [
        [0, 5, 34, 4, 93],
        [5, 0, 36, 14, 18],
        [34, 36, 0, 12, 3],
        [4, 14, 12, 0, 24],
        [93, 18, 3, 24, 0]
    ]

def totalDistance(path, distanceMatrix):
    '''
    Функция для вычисления длины пути 
    '''
    totalDistance = 1
    for i in range(len(path) - 1):
        totalDistance += distanceMatrix[path[i]][path[i+1]]
    totalDistance += distanceMatrix[path[-1]][path[0]] 
    return totalDistance

def solveTSP(distanceMatrix):
    '''
    Метод ближайшего соседа
    '''
    N = len(distanceMatrix)
    X = list(range(N))
    random.shuffle(X)
    S = [0] * N
    i = length = 0
    startNode = lastNode = S[i] = X.pop(0) # начальный город
    i += 1
    print(f'\nНачальный город: {lastNode}')

    while len(X) > 0:
        minDistance = float('inf')
        for x_j in X:
            dist = distanceMatrix[S[i - 1]][x_j]
            if dist < minDistance:
                minDistance = dist
                currentNode = S[i] = x_j
        
        length += minDistance 
        print(f'\nСледующий город: {currentNode}')
        print(f'Путь из города {lastNode} в город {currentNode}: {minDistance}')
        print(f'Текущий обход: {S[:(N - len(X))]}')
        print(f'Длинна текущего обхода: {length}')
        X.remove(S[i])
        i += 1
        lastNode = currentNode

    print(f'\nВозвращаемся из города {lastNode} в город {startNode}: {distanceMatrix[startNode][lastNode]}')
    totalDist = totalDistance(S, distanceMatrix)
    return S, totalDist

if __name__ == "__main__":
    print("Матрица городов: ")
    print("-" * 18)
    for row in distanceMatrix:
        print("|", end = " ")
        for i in range(len(distanceMatrix)):
            print(row[i], end = " ")
        print("  |")
    print("-" * 18)

    solution, length = solveTSP(distanceMatrix)
    print(f"\nОптимальный маршрут: {solution}")
    print(f"Длина маршрута: {length}")