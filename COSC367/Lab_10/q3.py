def construct_perceptron(weights, bias):
    """
    it takes a weight and bias and return either 1 or 0
    """
    def perceptron(input):
        a = sum([w * weights[index] for index, w in enumerate(input)])
        a = a + bias
        if a >= 0:
            return 1
        else:
            return 0
    
    return perceptron # this line is fine

weights = [2, -4]
bias = 0
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, 1]))