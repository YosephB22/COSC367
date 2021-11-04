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

def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]
s = (4, 6, 1, 2, 3, 5)
for state in greedy_descent(4, neighbours, cost):
    print(state)