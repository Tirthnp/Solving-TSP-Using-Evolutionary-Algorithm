from random import randint
import numpy as np
# cut-and-crossfill crossover for permutations
def permutation_cut_and_crossfill (parent1, parent2):

    offspring1 = []
    offspring2 = []

    rand=randint(1,len(parent1)-1)
    for i in range(0,len(parent1)):
        if(i<rand):
            offspring1.append(parent1[i])
            offspring2.append(parent2[i])
        else:
            x=get_next(parent2,parent2[i-1])

            while(len(offspring1)!=len(parent1)):
                if(x not in offspring1):
                    offspring1.append(x)
                x=get_next(parent2,x)

            x=get_next(parent1,parent1[i-1])
            while(len(offspring2)!=len(parent2)):
                if(x not in offspring2):
                    offspring2.append(x)
                x=get_next(parent1,x)
    return offspring1, offspring2

def order_crossover(parent1,parent2):

    offspring1=[0]*len(parent1)
    offspring2=[0]*len(parent1)
    rand=randint(0,len(parent1)-2)

    rand2=randint(rand+1,len(parent1)-1)

    for i in range(rand,rand2+1):
        offspring1[i]=parent1[i]
        offspring2[i]=parent2[i]
    counter=rand2+1
    while 0 in offspring2:
        if(counter == len(offspring1)):
            counter=0

        x=parent2[counter]
        while x in offspring1:
            x=get_next(parent2,x)
        offspring1[counter]=x

        y=parent1[counter]
        while y in offspring2:

            y=get_next(parent1,y)
        offspring2[counter]=y

        counter=counter+1

    return offspring1,offspring2





def get_next(array,value):

    inx=array.index(value)# np.where(array == value)#array.index(value)

    if(inx==len(array)-1):
        return array[0]
    return array[inx+1]
