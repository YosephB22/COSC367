import math
from collections import defaultdict
def euclidean_distance(v1, v2):
    """calculate the euclidean algorithm of two vectors"""
    euclidean = math.sqrt(sum([((vectors - v2[index]) ** 2)  for index, vectors in enumerate(v1)]))
    return euclidean
        
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

# print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))

print(euclidean_distance([0],[2]))