import numpy as np

distanceMatrix = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 10],
    [25, 30, 20, 10, 0]
])

def nearestCityAlgorithm(matrix): 
    # np.random.seed(42)  
    n = len(matrix)
    cities = list(range(1, n+1))
    solution = []
    candidates = []

    # currentCity = 2
    currentCity = np.random.choice(cities)
    cities.remove(currentCity)
    solution.append(currentCity)
    i = 1
    printStepSolution(i, candidates, currentCity, solution, 0, solution, 0)
    while cities:
        # print(cities)
        for idx, currentCity in enumerate(solution):
            for j in cities:
                candidates.append((idx, currentCity, j, matrix[currentCity-1][j - 1]))
    
        minDistance = min(candidates, key=lambda x: x[3])
        # print(minDistance)
        cityIdx, currentCity, chosenCity, distance = minDistance

        solution.insert(cityIdx+1, chosenCity)

        cities.remove(chosenCity)
        i += 1
        prettyPrintCandidates = {}
        for item in candidates:
            if item[1] in prettyPrintCandidates:
                if prettyPrintCandidates[item[1]][2] > item[3]:
                    prettyPrintCandidates[item[1]] = [item[1], item[2], item[3]]
            else:
                prettyPrintCandidates[item[1]] = [item[1], item[2], item[3]]
        prettyPrintCandidates = [prettyPrintCandidates[key] for key in prettyPrintCandidates]
        totalDistance = sum(matrix[solution[k] - 1][solution[k + 1] - 1] for k in range(len(solution) - 1))
        printStepSolution(i, [f"{item[0]} => {item[1]} = {item[2]}" for item in prettyPrintCandidates], chosenCity, solution, totalDistance, solution, totalDistance)

        candidates = [] 

    totalDistance += matrix[solution[-1] - 1][solution[0] - 1]
    solution.append(solution[0])

    printStepSolution(i + 1, [], None, solution, totalDistance, solution, totalDistance)

    return solution, totalDistance

def printStepSolution(step, candidates, chosenCity, currentPath, currentDistance, finalPath, finalDistance):
    print(f"\n№ шага {step}:")
    print(f"\tКандидаты: {candidates}")
    print(f"\tВыбранный город: {chosenCity}")
    print(f"\tТекущий путь: {currentPath}")
    print(f"\tТекущее расстояние: {currentDistance}")
    print(f"\tКонечный путь: {finalPath}")
    print(f"\tКонечное расстояние: {finalDistance}")


print("Матрица городов: ")
print("-" * 18)
for row in distanceMatrix:
    print("|", end = " ")
    for i in range(len(distanceMatrix)):
        print(row[i], end = " ")
    print("  |")
print("-" * 18)
solution, totalDistance = nearestCityAlgorithm(distanceMatrix)
print("\nКонечное решение:", solution)
print("Конечное расстояние:", totalDistance)