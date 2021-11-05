import math
def max_value(tree):
    """maximizing utilities based on what the other oppent chooses"""
    if type(tree) == int:
        return tree
    else:
        v = -math.inf
        for t in tree:
            v = max(v, min_value(t))
        return v

def min_value(tree):
    """minimizing utilities based on what the other oppent chooses"""
    if type(tree) == int:
        return tree
    else:
        v = math.inf
        for t in tree:
            v = min(v, max_value(t))
        return v


game_tree = [[1, 2], [3]]
print("Root utility for minimiser:", min_value(game_tree))
print("Root utility for maximiser:", max_value(game_tree))