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



def  max_action_value(game_tree):
    """
    given a tree return (best action, utility)
    """
    if type(game_tree) == int:
        return None, game_tree
    else:
        result = []
        for index, g in enumerate(game_tree):
            utility = min_value(g)
            result.append((index, utility))
        return max(result, key=lambda x: x[1])


def min_action_value(game_tree):
    """return a tuple where the first element is the best min action to consider,
    the second element ois the utility value"""
    if type(game_tree) == int:
        return None, game_tree
    else:
        result = []
        for index, tree in enumerate(game_tree):
            min_utility = max_value(tree)
            result.append((index, min_utility))
        return min(result, key=lambda x: x[1])





game_tree = [2, [-3, 1], 4, 1]


# action, value = min_action_value(game_tree)
# print("Best action if playing min:", action)
# print("Best guaranteed utility:", value)
# print()
action, value = min_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)