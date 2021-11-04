def is_valid_expression(object, function_symbols, leaf_symbols):
    """
    takes object and test if the expression is valid, the function should return true
    """

    if type(object) != list:
        if type(object) == int or (type(object) == str and object in leaf_symbols):
            return True
        else:
            return False
    else:
        if len(object) != 3:
            return False
        else:
            if type(object[0]) == str and object[0] in function_symbols:
                return (is_valid_expression(object[1], function_symbols, leaf_symbols) and 
                is_valid_expression(object[2], function_symbols, leaf_symbols))
            else:
                return False









# function_symbols = ['f', '+']
# leaf_symbols = ['x', 'y']
# expression = 'f'

# print(is_valid_expression(
#         expression, function_symbols, leaf_symbols))

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['f', 1, 0]

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))
