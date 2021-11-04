from itertools import combinations
def n_queens_neighbours(state):
    """takes a state (total assignment) for an n-queen problem and returns a sorted list 
    of states that are the neighbours of the current assignment. 
    A neighbour is obtained by swapping the position of two numbers in the given permutation.
    """
    final_swapped = []
    comb = combinations(state, 2)
    all_comb = [c for c in comb]
    for combination in all_comb:
        new_state = list(state)
        first_swap_index = new_state.index(combination[0])
        second_swap_index = new_state.index(combination[1])
        new_state[first_swap_index], new_state[second_swap_index] = new_state[second_swap_index], new_state[first_swap_index]
        new_state = tuple(new_state)
        final_swapped.append(new_state)
    return sorted(final_swapped)
        
print(n_queens_neighbours((1, 3, 2)))
