def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        # Complete (a line or two)
        sum_vector = sum([value * weights[index] for index, value in enumerate(input)])
        a = bias + sum_vector  
        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        if a >= 0:
            return 1
        else:
            return 0
    
    return perceptron # this line is fine





weights = [0.5, 0.5]
bias = 0
learning_rate = 0.5
perceptron = construct_perceptron(weights, bias)
print(perceptron([1, -1]))
examples = [
    ([1, 1],   0),    # index 0 (first example)
    ([2, 0],   1),
    ([1, -1],  0),
    ([-1, -1], 1),
    ([-2, 0],  0),
    ([-1, 1],  1),
]
