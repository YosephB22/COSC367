import math
from collections import defaultdict
# euclidean distance
def euclidean_distance(v1, v2):
    """calculate the euclidean algorithm of two vectors"""
    return math.sqrt(sum([(a-b)**2 for a,b in zip(v1, v2)]))

def majority_element(labels):
    """takes a sets of outputs abd combine them in order to derive a new prediction"""
    binary = defaultdict(int)
    for l in labels:
        if l not in binary:
            binary[l] = 1
        else:
            binary[l] += 1
    most_frequent = max(binary.items(), key=lambda x: x[1])
    return most_frequent[0]

def knn_predict(input, examples, distance, combine, k):
    """
    that takes an input and predicts the output by combining the output of the k nearest neighbours
    """
    new_example = []
    for index, (number, operator) in enumerate(examples):
        euclidean = distance(input, number)
        new_example.append((euclidean, operator))
    new_example = sorted(new_example)

    selected_neighbour = new_example[:k]
    for index, example in enumerate(new_example[k:]):
        if selected_neighbour[-1][0] == example[0]:
            selected_neighbour.append(example)
        else:
            break
    label = [oper for (dstance, oper) in selected_neighbour]
    most_common = combine(label)
    return most_common

examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()