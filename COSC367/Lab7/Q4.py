from itertools import permutations
def n_queens_neighbours(state):
    """takes a state (total assignment) for an n-queen problem and returns a sorted list 
    of states that are the neighbours of the current assignment. 
    A neighbour is obtained by swapping the position of two numbers in the given permutation.
    """
    neighbour = []
    for i, row in enumerate(state):
        for j, col in enumerate(state):
            list_state = list(state)
            #swaping two elements
            if i < j:
                list_state[i], list_state[j] = list_state[j], list_state[i]
                neighbour.append(tuple(list_state))
    return sorted(neighbour)


from itertools import combinations

def n_queens_cost(state):
    """return the number of confilict in the state"""
    conflictNum = 0
    target = [i for i in range(1, len(state) + 1)]
    comb = combinations(target, 2)
    all_comb = [c for c in comb]
    for col1, col2 in all_comb:
        col_difference = col2 - col1
        row1, row2 = state[col1 - 1], state[col2 - 1]
        row_difference = abs(row2 - row1)
        if row_difference == col_difference:
            conflictNum += 1
    return conflictNum

def greedy_descent(initial_state, neighbours, cost):
    """takes an initial state and two functions to compute the neighbours 
    and cost of a state, and then iteratively improves 
    the state until a local minimum (which may be global) is reached.
    """
    current_state = initial_state
    listOfState = [current_state]
    while len(neighbours(current_state)):
        minimum_neighbour = min([(n, cost(n)) for n in neighbours(current_state)], key=lambda x: x[1])
        if (minimum_neighbour[1]) < cost(current_state):
            current_state = minimum_neighbour[0]
            listOfState.append(current_state)
        else:
            return listOfState
    return listOfState


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    """kjhkj"""
    state = random_state()
    found = False
    while not found:
        result = greedy_descent(state, neighbours, cost)
        for s in result:
            print(s)
        costOfState = cost(result[-1])
        if costOfState > 0:
            print("RESTART")
            state = random_state()
        else:
            found = True
        


import random

N = 20
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))   

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)