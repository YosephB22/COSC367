import math
def max_value(tree, result=None):
    """return the maximum value given what min would choose"""
    
    if result == None:
        result = -math.inf
    if type(tree) == int:
        return tree
    else:
        for maxi in tree:
            result = max(result, min_value(maxi))
    return (result)
def min_value(tree, result=None):
    """return the minimum value given what the max_value function would return"""
    if result == None:
        result = math.inf
    if type(tree) == int:
        return tree
    else:
        for index, maxi in enumerate(tree):
            result = min(result, max_value(maxi))
    return (result)

def  max_action_value(game_tree):
    """return a tuple where the first element is the best max action to consider,
    the second element ois the utility value"""
    if type(game_tree) == int:
        return None, game_tree
    else:
        result = []
        for index, tree in enumerate(game_tree):
            max_utility = min_value(tree)
            result.append((index, max_utility))
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





game_tree = [[1, 2], [3, 4]]

# action, value = min_action_value(game_tree)
# print("Best action if playing min:", action)
# print("Best guaranteed utility:", value)
# print()
action, value = max_action_value(game_tree)
print("Best action if playing max:", action)
print("Best guaranteed utility:", value)