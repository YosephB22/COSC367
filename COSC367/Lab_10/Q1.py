import math
from collections import defaultdict
# euclidean distance
def euclidean_distance(v1, v2):
    """calculate the euclidean algorithm of two vectors"""
    return math.sqrt(sum([(a-b)**2 for a,b in zip(v1, v2)]))

# manhattan distance
def Manhnattan_distance(v1, v2):
    """calculating the manhnattan distance"""
    return sum([abs(a-b) for a,b in zip(v1, v2)])

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

# define data
row1 = [10, 20, 15, 10, 5]
row2 = [12, 24, 18, 8, 7]
print(Manhnattan_distance(row1,row2))