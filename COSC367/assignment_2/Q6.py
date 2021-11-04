import random
# Q5 function
def generate_rest(initial_sequence, expression, length, result=None):
    """generate a list of integers"""
    i = len(initial_sequence)
    initial = initial_sequence.copy()
    j = len(initial)
    binding = {"i": len(initial), "x":initial[-2], "y":initial[-1], 
    "+": lambda x, y: x+y, 
    "*": lambda x, y: x*y, 
    "-": lambda x, y: x-y}
    for index in range(length):
        result = evaluate(expression, binding)
        initial.append(result)
        binding["i"] = len(initial)
        binding["x"] = initial[-2]
        binding["y"] = initial[-1]
    return initial[i:]

# Q4 function
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

# Q3 function
def evaluate(expression, bindings):
    """jhbkj"""
    if type(expression) == int:
        return expression 
    elif type(expression) == str:
        return bindings[expression]
    else:
        return bindings[expression[0]](evaluate(expression[1], bindings), evaluate(expression[2], bindings))

def predict_rest(sequence):
    """finish the sequence"""
    function_symbols = ['*', '+', '-']
    constant_leaves =  list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 3
    initial_sequence = sequence[:3]
    remaining_sequence = sequence[3:]
    for _ in range(100000):
        expression = random_expression(function_symbols, leaves, max_depth)
        new_result = generate_rest(initial_sequence, expression, len(remaining_sequence))
        if new_result == remaining_sequence:
            break
    new_result = generate_rest(sequence, expression, 5)
    return new_result
            
sequence = [3, 2, 3, 6, 11, 18, 27, 38]
print(predict_rest(sequence))