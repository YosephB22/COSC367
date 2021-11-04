import random
import numpy as np
from collections import defaultdict
def roulette_wheel_select(population, fitness, r):
    """  
    population = list of individuals.
    fitness = takes the individual and return a value, that value will indicate how good/bad the individula are.
    r = random floating number from 0 to 1.
    select and return an individual from the population using the roulete wheel selection mechanisim.
    """
    T = sum([fitness(i) for i in population])
    # N = r * T
    probabilityIndividual = []
    sums = 0
    for f in population:
        sums += fitness(f)
        probabilityIndividual.append(sums)
    for index, running_total in enumerate(probabilityIndividual):
        if running_total > r:
            return population[index]




population = [1, 2, 3, 4, 5, 6]

def fitness(x):   
    default = {'1': 8, '2':2, '3':17, '4':7, '5':4, '6':11}
    x = str(x)
    return default[x]
print(roulette_wheel_select(population, fitness, 23))
# population = ['a', 'b']

# def fitness(x):
#     return 1 # everyone has the same fitness

# for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
#     print(roulette_wheel_select(population, fitness, r))