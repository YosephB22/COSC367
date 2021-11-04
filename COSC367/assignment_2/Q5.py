import operator
def evaluate(expression, bindings):
    """jhbkj"""
    if type(expression) == int:
        return expression 
    elif type(expression) == str:
        return bindings[expression]
    else:
        return bindings[expression[0]](evaluate(expression[1], bindings), evaluate(expression[2], bindings))


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


initial_sequence = [4, 6, 8, 10]
expression = ['+', 2, 'y']
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))