import math
import random

def MPS(fitness, mating_pool_size):

    selected_to_mate = []
    cumulative_fitness=[]
    total=0
    total_frequency=0
    for i in fitness:
        total +=i
    for i in fitness:
        temp=float(i)/float(total)
        total_frequency += temp
        cumulative_fitness.append(total_frequency)
    current_member=0
    i=0
    random_range=1.0/float(mating_pool_size)
    r = random.uniform(0.0, random_range)
    while(current_member< mating_pool_size):
        while (r<=cumulative_fitness[i]):
            selected_to_mate.append(i)
            r= r+1.0/float(mating_pool_size)
            current_member=current_member+1
        i+=1


    return selected_to_mate


def random_uniform (population_size, mating_pool_size):

    selected_to_mate = []
    while(len(selected_to_mate) < mating_pool_size):
        selected_to_mate.append(random.randint(0,population_size-1))

    return selected_to_mate
