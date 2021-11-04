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
        for maxi in tree:
            result = min(result, max_value(maxi))
    return (result)







game_tree = [[1, 2], [3]]

print(min_value(game_tree))
print(max_value(game_tree))