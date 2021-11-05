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




print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))
print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
