import random

def monteCarloMethod(N, searchSpace, fixedSpace):
    maxAdaptation = 0
    maxSolution = None
    
    if fixedSpace:
        N = 32
    
    for i in range(N):
        print ("\t№ текущего шага: ", i + 1)
        
        if fixedSpace:
            randomSolution = searchSpace[i]
        else:
            randomSolution = random.choice(searchSpace) 
        
        adaptation = int(random.choice(searchSpace), 2)
        maxChange = ""

        if adaptation > maxAdaptation:
            maxAdaptation = adaptation
            maxSolution = randomSolution
            maxChange = "! Максимум изменён"
            print (maxChange)
        
        print ("\t\tТекущий максимум приспособленности: ", maxAdaptation)
        print ("\t\tТекущая лучшая кодировка: ",  maxSolution)
        print ("\t\tВыбираемая кодировка на текущем шаге: ", randomSolution)
        print ("\t\tПриспособленность выбираемой кодировки: ", adaptation)
        print ("-"*100)
    print("\tРешение: ")
    print(f"\t\tПриспособленность: {maxAdaptation}\n\t\tКодировка: {maxSolution}")

if __name__ == "__main__":
    L = 15
    N = 15
    searchSpace = [format(x, 'b').zfill(L) for x in range(2**L)]

    print ("Вывод первых 32 кодировок: ")
    monteCarloMethod(N, searchSpace, True)
    print ("Случайное поле поиска: ")
    monteCarloMethod(N, searchSpace, False)