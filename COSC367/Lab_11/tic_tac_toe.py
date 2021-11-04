def optimal_move(board, player):
    result = []
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col not in ["X", "O"]:
                result.append((row_index, col_index))
    return min(result, key=lambda x: (x[0], x[1]))


board = [
    ['X', '.', '.'], 
    ['.', '.', '.'],
    ['.', '.', '.']
]
player = 'O'
print("player:", player, "playes", optimal_move(board, player))
