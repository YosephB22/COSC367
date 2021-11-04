def depth(expression):
    """return the depth of the expression"""
    if type(expression) != list:
        return 0
    else:
        return 1 + max(depth(expression[1]), 
        depth(expression[2]))





e = ['add', ['add', 22, 'y'], 'x']
print(depth(e))