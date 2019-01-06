import numpy as np
import time

import initialization
import evaluation
import parentSelection
import mutation
import survivorSelection
import random
import recombination
import tsp_plot
import matplotlib.pyplot as plt
def main():

    start=time.time()
    f = open("TSP_WesternSahara_29.txt", "r")
    #f = open("TSP_Uruguay_734.txt","r")
    #f= open("TSP_Canada_4663.txt","r")
    #f = open("D_38.txt","r")

    cities = []
    i=0
    #print(f.readline())
    for val in f:
        c=val.split()
        c=c[1:]
        c=np.float_(c)
        cities.append(c)
    pop_size=100
    gen_limit=300
    mating_pool_size=int(pop_size*0.5)
    fitness=[]
    averageFitness = []
    bestFitness = []
    gen=0
    mut_rate = 0.7
    xover_rate = 0.9
    switch=0
    count=0
    best=[]
    best_fitness=-1000000000


    processedDistance = evaluation.processDistance(cities);
    if len(cities)>200:
        population=initialization.permutation(pop_size,len(cities))
    else:
        population=initialization.initialPop(cities,pop_size,processedDistance)



    fitness=evaluation.fitness_evaluation(population)
    print("generation", gen, ": best fitness", max(fitness), "average fitness", sum(fitness)/len(fitness))
    while gen < gen_limit:
        if switch > 1 :
            parents_index = parentSelection.random_uniform(pop_size, mating_pool_size)
        else:
            parents_index = parentSelection.MPS(fitness, mating_pool_size)


        # in order to randomly pair up parents
        random.shuffle(parents_index)

        # reproduction
        offspring =[]
        offspring_fitness = []
        i= 0 # initialize the counter for parents in the mating pool
        # offspring are generated using selected parents in the mating pool
        while len(offspring) < mating_pool_size:

            # recombination
            if random.random() < xover_rate:
                if switch>1:
                    off1,off2 = recombination.order_crossover(population[parents_index[i]], population[parents_index[i+1]])
                else:
                    off1,off2 = recombination.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]])
                #off1,off2 = recombinationsahil.permutation_cut_and_crossfill(population[parents_index[i]], population[parents_index[i+1]])
            else:
                off1 = population[parents_index[i]].copy()
                off2 = population[parents_index[i+1]].copy()

            # mutation
            if random.random() < mut_rate:
                off1 = mutation.permutation_swap(off1)
                #off1=mutation.scramble_mutation(off1)
            if random.random() < mut_rate:
                off2 = mutation.permutation_swap(off2)
                #off2=mutation.scramble_mutation(off2)


            offspring.append(off1)
            offspring_fitness.append(evaluation.fitness_evaluation_child(off1))
            offspring.append(off2)
            offspring_fitness.append(evaluation.fitness_evaluation_child(off2))
            i = i+2  # update the counter


        if switch > 1 :
            population, fitness = survivorSelection.random_uniform(population, fitness, offspring, offspring_fitness)
            count=count+1
        else:
            population, fitness = survivorSelection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
        if count >1:
            switch=0
            count=0
        gen = gen + 1  # update the generation counter
        ave=sum(fitness)/len(fitness)
        m=max(fitness)
        print("generation", gen, ": best fitness",-m, "average fitness",-ave )
        if m>best_fitness:
            best=population[fitness.index(m)]
            best_fitness=m
        print("best fitnses yet :",-best_fitness)
        if int(m)==int(ave):

            switch=switch+1

        averageFitness.append(-ave)
        bestFitness.append(-m)
    end=time.time() - start
    print("Time taken :",end)
    tsp_plot.plotTSP(best,cities,1)
    geneticAlgorithmPlot(averageFitness)
    geneticAlgorithmPlot(bestFitness)
def geneticAlgorithmPlot(fitness):

    plt.plot(fitness)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()


main()
