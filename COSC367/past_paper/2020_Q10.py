def select(population, error, max_error, r):
    """
    return the individidual who has a maximum error possible, close to the max_error
    error = individual firtness.
    r = random number 0 >= r <= 1.
    population = individual.
    """
    fitness = [max_error - error(i) for i in population]
    running_total = []
    sums = 0
    for f in fitness:
        sums += f
        running_total.append(sums)
    N = r * running_total[-1]
    for index, individual in enumerate(running_total):
        if individual > N:
            return population[index]


population = ['a', 'b']

def error(x):
    return {'a': 14,
            'b': 12}[x]

max_error = 15

for r in [0.26, 0.5, 0.9]:
    print(select(population, error, max_error, r))

# since the fitness of 'a' is 1 and the fitness of 'b' is 3,
# for r's below 0.25 we get 'a', for r's above it we get 'b'.