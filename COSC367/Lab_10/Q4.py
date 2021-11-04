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
    """goes through each input, compute perception and check that with the expected_outputs"""
    # guesed_right keeps tracks of how many perception we got right predicting
    guesed_right = 0
    for index, value in enumerate(inputs):
       if classifier(value) == expected_outputs[index]:
           guesed_right += 1
    return guesed_right / len(expected_outputs)



perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))