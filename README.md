# Solving-TSP-Using-Evolutionary-Algorithm
## ● PARAMETERS OF GENETIC ALGORITHM:
* ○ Gene: a city in(x, y) coordinates
* ○ Individual (Chromosome): Each individual have chromosomes as permutation of number
of cities. For example if the number of cities= 4, then [2,3,4,1] could be an example of an
individual.
* ○ Population : a collection of possible routes (i.e., collection of individuals); It says how
many chromosomes are in population. Depends on the type of encoding and the problem.
If there are only few chromosomes, then GA would have a few possibilities to perform
crossover and only a small part of search space is explored.If there are many chromosomes
then GA slows down.
* ○ Parent : route which are combined to create new Route.
* ○ Mutation pool : .It may be defined as a small random tweak in the chromosome, to get a
new offsprings. It is used to maintain and introduce diversity in our population and is
usually applied with a low probability ( p m ) If the probability is high, the GA gets reduced
to a random mutation.
* ○ Fitness: The fitness simply defined is a function which takes a candidate solution to the
problem as input and produces as output how shortes and fit ,“optimal” the solution is with
respect to the problem in consideration
* ○ Survival : It is the process of determining the individual that will proceed to next
generation. Here we have used MU+Lambda, MU,Lambda or Replacement and random
uniform.
