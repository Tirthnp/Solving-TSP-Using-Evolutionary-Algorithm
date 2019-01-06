import numpy
import numpy as np
import time

processedDistance = {}
minimum = {}
def cities_distance (cities):
    total=0

    for i in range(0,len(cities)-1):
        d=[]
        for j in range(i,len(cities)):
            dist=sqrt_sum(cities[i],cities[j])
            d.append(dist)
        distance_vector.append(d)

def processDistance(cities):
    for i in range(len(cities)):
        for j in range(len(cities)):
            dist = sqrt_sum(cities[i],cities[j])
            processedDistance[(i+1),(j+1)] =dist
    return processedDistance

def fitness_evaluation(population):
    fitness = [0]*len(population)
    for count, individual in enumerate(population):
        for i in range(len(individual)-1):
            dist = processedDistance[min(individual[i],individual[i+1]),max(individual[i],individual[i+1])]
            fitness[count]+= dist
        dist = processedDistance[min(individual[len(individual)-1],individual[0]),max(individual[len(individual)-1],individual[0])]
        fitness[count]+=dist
    return list(numpy.array(fitness)*-1)


def fitness_evaluation_child(offspring):
    fitness = 0
    for i in range(len(offspring)-1):
        dist = processedDistance[min(offspring[i],offspring[i+1]),max(offspring[i],offspring[i+1])]
        fitness += dist
    dist = processedDistance[min(offspring[len(offspring)-1],offspring[0]),max(offspring[len(offspring)-1],offspring[0])]
    fitness += dist
    return fitness*-1
def sqrt_sum(a,b):
    a_min_b = a - b
    return (numpy.sqrt(numpy.sum(a_min_b**2,axis=0)))
