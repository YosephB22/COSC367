import math
from collections import defaultdict

def majority_element(labels):
    """return the most frequence number"""
    dictionary = defaultdict(int)
    for l in labels:
        if l in dictionary:
            dictionary[l] += 1
        else:
            dictionary[l] = 1
    most_common = max([value for key, value in dictionary.items()])
    for k, v in dictionary.items():
        if dictionary[k] == most_common:
            return k

def euclidean_distance(v1, v2):
        """calculate the euclidean algorithm of two vectors"""
        return math.sqrt(sum([(a-b)**2 for a,b in zip(v1, v2)]))
        # print(v1, v2)
        # euclidean = math.sqrt(sum([((vectors - v2[index]) ** 2)  for index, vectors in enumerate(v1)]))
        # return euclidean

def knn_predict(input, examples, distance, combine, k):
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
    ([1], 5),
    ([2], -1),
    ([5], 1),
    ([7], 4),
    ([9], 8),
]

def average(values):
    return sum(values) / len(values)

distance = euclidean_distance
combine = average

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
    print()