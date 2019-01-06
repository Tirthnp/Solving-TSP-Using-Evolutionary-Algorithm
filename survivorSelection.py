import random

# (mu+lambda) selection
def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    population = []
    fitness = []

    lamda_plus_mu=current_pop+offspring
    lamda_plus_mu_fitness=current_fitness+offspring_fitness

    lamda_plus_mu_fitness,lamda_plus_mu=population_sorter_with_fitness(lamda_plus_mu_fitness,lamda_plus_mu)
    population=lamda_plus_mu[:len(current_pop)]
    fitness=lamda_plus_mu_fitness[:len(current_pop)]



    return population, fitness


# use offspring to replace the same number of the worst individuals in the current population
def replacement(current_pop, current_fitness, offspring, offspring_fitness):

    population = []
    fitness = []

    current_fitness,current_pop=population_sorter_with_fitness(current_fitness,current_pop)
    offspring_fitness,offspring=population_sorter_with_fitness(offspring_fitness,offspring)
    population=current_pop[:(len(current_pop)-len(offspring))]+offspring
    fitness=current_fitness[:(len(current_fitness)-len(offspring_fitness))]+offspring_fitness


    return population, fitness

# randomly uniformly pick individuals from the current population and new offspring
def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):

    population = []
    fitness = []


    while(len(population)<len(current_pop)):
        rand=random.randint(0,1)
        if rand==1:
            r=random.randint(0,len(current_pop)-1)
            population.append(current_pop[r])
            fitness.append(current_fitness[r])
        else:
            r=random.randint(0,len(offspring)-1)
            population.append(offspring[r])
            fitness.append(offspring_fitness[r])

    return population, fitness
def population_sorter_with_fitness(fitness,population):
    ## Uses BubbleSort
    for iter_num in range(len(fitness)-1,0,-1):
        for idx in range(iter_num):
            if fitness[idx]<fitness[idx+1]:
                temp = fitness[idx]
                temp1 = population[idx]
                fitness[idx] = fitness[idx+1]
                population[idx]=population[idx+1]
                fitness[idx+1] = temp
                population[idx+1]=temp1
    return fitness,population
