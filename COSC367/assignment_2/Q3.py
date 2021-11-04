def evaluate(expression, bindings):
    """jhbkj"""
    if type(expression) == int:
        return expression 
    elif type(expression) == str:
        return bindings[expression]
    else:
        return bindings[expression[0]](evaluate(expression[1], bindings), evaluate(expression[2], bindings))

import operator

bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
expression = ['add', ['add', 22, 'y'], 'x']
print(evaluate(expression, bindings))