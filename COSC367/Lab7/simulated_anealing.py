def simulated_anealing(problem, max):
    """
    problem = the problem we are trying to sove.
    max = maximum number of times we might want to run the simulated anealing.
    """
    current = "initial state of the problem"
    for i in range(1, max):
        # T = Temprature(i)
        neightbour = "random neighbour of current"
        # delta+E is how much better neighbour is than current
        delta_E = current - neightbour
        # if delta_E > 0, the neighbour is better than our current state
        # else, its worse.
        if delta_E > 0:
            current = neightbour
            # calculating the probability to select a worst neighbour
        # with probability e^E/T set current = neighbour
    return current