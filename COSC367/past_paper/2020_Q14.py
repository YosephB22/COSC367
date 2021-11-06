from collections import defaultdict
# manhattan distance
def Manhnattan_distance(v1, v2):
    """calculating the manhnattan distance"""
    return sum([abs(a-b) for a,b in zip(v1, v2)])

def estimate(time, observations, k):
    """takes a time and observation and produce a tempreture estimate"""
    result = []
    for index, (t, temp) in enumerate(observations):
        time_distance = Manhnattan_distance([t], [time])
        result.append((time_distance, temp))
    result = sorted(result, key=lambda x: x[0])

    selected_neighbour = result[:k]
    for index, example in enumerate(result[k:]):
        if selected_neighbour[-1][0] == example[0]:
            selected_neighbour.append(example)
        else:
            break
    sum_temp = sum([temprature[1] for temprature in selected_neighbour])
    return sum_temp/len(selected_neighbour)

observations = [
    (-1, 1),
    (0, 0),
    (-1, 1),
    (5, 6),
    (2, 0),
    (2, 3),
]

for time in [-1, 1, 3, 3.5, 6]:
    print(estimate(time, observations, 2))