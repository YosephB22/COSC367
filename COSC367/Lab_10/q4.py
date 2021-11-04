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


def accuracy(classifier, inputs, expected_outputs):
    """takes some example inputs and compare it with the expected output"""
    accuracy = 0
    for index, w in enumerate(inputs):
        perc = (classifier(w))
        if perc == expected_outputs[index]:
            accuracy += 1
    return accuracy / len(expected_outputs)


perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))