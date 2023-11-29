import random

def monteCarloMethod(L, N, searchSpace):
    '''
    Реализация метода Монте-Карло
    '''
    maxAdaptation = 0
    maxSolution = None

    for i in range(N):
        randomSolution = random.choice(searchSpace)
        adaptation = int(random.choice(searchSpace), 2)
        maxChange = ""
        if adaptation > maxAdaptation:
            maxAdaptation = adaptation
            maxSolution = randomSolution
            maxChange = "Максимум изменён"
            print (maxChange)
        
        print ("№ текущего шага: ", i + 1)
        print ("\tТекущий максимум приспособленности: ", maxAdaptation)
        print ("\tТекущая лучшая кодировка: ",  maxSolution)
        print ("\tВыбираемая кодировка на текущем шаге: ", randomSolution)
        print ("\tПриспособленность выбираемой кодировки: ", adaptation)
        print ("-"*18)
    print("Решение: ")
    print(f"\tПриспособленность: {maxAdaptation}\n\tКодировка: {maxSolution}")

if __name__ == "__main__":
    L = 15
    N = 15
    searchSpace = [format(x, 'b').zfill(L) for x in range(2**L)]

    monteCarloMethod(L, N, searchSpace)