import random
def random_expression(function_symbols, leaves, max_depth, index=None):
    """generate a random expression"""
    if index == None:
        index = 0
    if index == max_depth:
        return random.choice(leaves)
    else:
        coin = [0, 1]
        random.choice(coin)
        if random.choice(coin) == 0:
            return[random.choice(function_symbols), random_expression(function_symbols, leaves, max_depth, index+1),
            random_expression(function_symbols, leaves, max_depth, index+1)]
        else:
            return random.choice(leaves)


# All the generated expressions must be valid

function_symbols = ['f', 'g', 'h']
constant_leaves =  list(range(-2, 3))
variable_leaves = ['x', 'y', 'i']
leaves = constant_leaves + variable_leaves
max_depth = 4

for _ in range(10000):
    expression = random_expression(function_symbols, leaves, max_depth)
    print(expression)