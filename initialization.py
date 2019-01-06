import random
import copy
import evaluation
import numpy as np
import time

def permutation(pop_size, chrom_length):
    population = []

    while(len(population)!=pop_size):
        individual=np.random.permutation(chrom_length)
        individual=individual+1
        population.append(list(individual))
    return(population)





def initialPop(data,popSize,lookup):
    
    cityList = list(range(1,len(data)+1))
    newL = copy.deepcopy(cityList)
    val = None
    population = []
    for i in range(popSize):
        if (len(newL) == 0):
            individual = np.random.choice(cityList,size=len(cityList),replace =False)
        else:
            x = np.random.randint(low=0,high = len(newL))
            individual = [newL[x]]
            newL.pop(x)
            for c in range(len(cityList)):
                m = 1000000000000000000000000000000
                for i in lookup:
                    if int(i[0])==int(x):
                        if (int(i[1]) not in individual):
                            if lookup[i]<m:
                                val = i[1]
                                m = lookup[i]
                x = val
                individual.append(int(val))
            individual.pop()
        if individual[0]==individual[1]:
            individual.pop(0)
            individual.append(24)
        population.append(list(individual))

    return population
