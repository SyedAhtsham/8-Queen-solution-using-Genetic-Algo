import random
import numpy as numpy


class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value


maxFitness = 28
initialPopulation = [[3, 2, 7, 5, 2, 4, 1, 1], [2, 4, 7, 4, 8, 5, 5, 2], [3, 2, 5, 4, 3, 2, 1, 3], [2, 4, 4, 1, 5, 1, 2, 4]]
nextGeneration = []
tempPopulation = list()
solution = []

fitnessValues = [0]
fitnessPercentage = my_dictionary()
CUTOFF = 3




def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res



def generateInitialPopulation():
    global initialPopulation

    for i in range(4):
        initialPopulation.append(Rand(1, 8, 8))


def fitnessFunction():
    global initialPopulation
    global fitnessValues
    global fitnessPercentage
    global solution
    fitnessValues.clear()

    individualScore = 0
    totalFitness = 0

    for i in range(4):
        for j in range(8):
            l = 0
            for k in range(j+1, 8):
                l +=1
                if initialPopulation[i][j] == initialPopulation[i][k]:
                    continue
                elif initialPopulation[i][j]+l == initialPopulation[i][k]:
                    continue
                elif initialPopulation[i][j]-l == initialPopulation[i][k]:
                    continue
                else:
                    individualScore+=1



        if individualScore == maxFitness:
            solution = initialPopulation[i]
        fitnessValues.append(individualScore)
        totalFitness += individualScore
        individualScore = 0


    for i in range(4):
        fitnessPercentage.add(i, round((fitnessValues[i]/totalFitness) * 100))



def crossOver():
    global fitnessPercentage
    global initialPopulation
    global tempPopulation


    fitnessPercentageSorted = sorted(fitnessPercentage.items(), key=lambda kv: kv[1])
    fitnessPercentageSorted.reverse()
    rankedChromosomes = list()
    # print(initialPopulation)
    for i in range(4):
        rankedChromosomes.append(initialPopulation[fitnessPercentageSorted[i][0]])




    tempPopulation.append(rankedChromosomes[0][0:CUTOFF] + rankedChromosomes[1][CUTOFF:8])
    tempPopulation.append(rankedChromosomes[1][0:CUTOFF] + rankedChromosomes[0][CUTOFF:8])
    tempPopulation.append(rankedChromosomes[1][0:8-CUTOFF] + rankedChromosomes[2][8-CUTOFF:8])
    tempPopulation.append(rankedChromosomes[2][0:8-CUTOFF] + rankedChromosomes[1][8-CUTOFF:8])



    # print(tempPopulation)



    # print(rankedChromosomes)
    # print(fitnessPercentageSorted)



def mutation():
    global tempPopulation
    global initialPopulation
    mutationProb = 0.8
    for i in range(4):

        if random.random() < mutationProb:
            gene = random.randint(0, 8-1)
            allele = random.randint(1, 8)
            tempPopulation[i][gene] = allele



    initialPopulation = tempPopulation.copy()
    tempPopulation.clear()




def main():
    generateInitialPopulation()

    noOfGen = 0
    while not maxFitness in fitnessValues:
        fitnessFunction()
        crossOver()
        mutation()
        noOfGen+=1

    print("\n")
    print("MY SOLUTION after "+str(noOfGen)+" number of Generations: ")
    print(solution)


if __name__ == "__main__":
    main()