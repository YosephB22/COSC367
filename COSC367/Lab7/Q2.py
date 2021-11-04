from itertools import combinations

def n_queens_cost(state):
    """return the number of confilict in the state
    if the difference between the ro and col is the same, then there is a conflict"""
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

print(n_queens_cost((1, 2, 3)))
