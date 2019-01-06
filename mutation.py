import copy
from random import randint
import random
# mutate a permutation
def permutation_swap (individual):

    mutant = individual

    # student code begin
    rand=randint(0,len(individual)-1)
    rand1=randint(0,len(individual)-1)
    while(rand1==rand):
        rand1=randint(0,len(individual)-1)
    mutant[rand],mutant[rand1]=mutant[rand1],mutant[rand]

    # student code end

    return mutant
def scramble_mutation(individual):

    mutant = individual

    rand=randint(0,len(mutant)-2)
    rand2=randint(rand+1,len(mutant)-1)
    while(rand==rand2):
        rand2=randint(rand+1,len(mutant)-1)
    part1=mutant[:rand]
    part2=mutant[rand2:]
    scram=mutant[rand:rand2]

    random.shuffle(scram)

    for i in scram:
        part1.append(i)
    for i in part2:
        part1.append(i)

    return part1
