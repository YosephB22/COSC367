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

def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    """return a tuple of updated weights and bias"""
    found = [False for _ in range(len(training_examples))]
    while max_epochs >= 0:
        found = [False for _ in range(len(training_examples))]
        for index, (inputs, expected_output) in enumerate(training_examples):
            inputs = list(inputs)
            classifier = construct_perceptron(weights, bias)
            perceptron = classifier(inputs)
            if perceptron != expected_output:
                print(f"pattern, output, target at index {index}: {inputs}, {perceptron}, {expected_output}")
                weights[0] = weights[0] + (learning_rate * inputs[0]) * (expected_output - perceptron)
                weights[1] = weights[1] + (learning_rate * inputs[1]) * (expected_output - perceptron)
                bias = bias + (learning_rate * ((expected_output - perceptron)))
                print(f"updating the weight and bias to: {weights} {bias}")
            else:
                found[index] = True
                print(f"pattern, output, target at index {index}: {inputs}, {perceptron}, {expected_output}")
        print(max_epochs)
        print()
        max_epochs -= 1
        if all(found):
            return weights, bias 
    return weights, bias

weights = [1.0, 1.0]
bias = -2.0
learning_rate = 0.5
examples = [
    ([0, 4],   0),   # index 0 (first example)
    ([-2, 1],   1),
    ([3, 5],  0),
    ([1, 1], 1)
]
max_epochs = 500

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")