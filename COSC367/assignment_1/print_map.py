from search import *
import math
import re
import heapq
class RoutingGraph(Graph):
    """navigating an agent to a call point that are time-wise closest to each other.
    S or [0-9] = agent.
    if agent == S --> not fuel needed.
    if agent == [0-9] --> needs fuel.
    G == Goal(distination) --> call points.
    can move N, E, S, W, respectfully.
    action of cost ==  5 units of time.
    can take action 'Fuel up' iff agent is at 'F'(fills the fuel to 9, maximum).
    state = (row, column, fuel).
    """
    def __init__(self, map_str, goal_node=[]):
        matrix = []
        element = []
        self.map_str = map_str
        #constructing matrix starts
        for i in self.map_str:
            if i != '\n':
                element.append(i)
            else:
                matrix.append(element)
                element = []
        #constructing matrix ends     
        self.map_str = matrix
        self.goal_node = goal_node
    def starting_nodes(self):
        start = []
        for row, value in enumerate(self.map_str):
            for col, v in enumerate(value):
                found = re.search("[0-9]", self.map_str[row][col])
                if found:
                    start.append((row, col, int(found.group())))
                if self.map_str[row][col] == "S":
                    start.append((row, col, math.inf))
                if self.map_str[row][col] == "G":
                    self.goal_node += [(row, col)]
        return start
    def is_goal(self, node):
        row, cols, fuel = node
        return self.map_str[row][cols] == "G"
    
    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""
        arcs = []
        (rows, cols, fuel) = tail_node
        for actions in [('N' , -1, 0), ('E' ,  0, 1), ('S' ,  1, 0), ('W' ,  0, -1)]:
            direction, row, col = actions
            new_row = rows + row
            new_col = cols + col
            if fuel > 0:
                if self.map_str[new_row][new_col] not in ['+', '-', 'X', "|"]:
                    arcs.append(Arc(tail_node, (new_row, new_col, (fuel - 1)), direction, 5))
        if self.map_str[rows][cols] == "F" and fuel < 9:
            arcs.append(Arc(tail_node, (rows, cols, 9), "Fuel up", 15))
        return arcs
    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""
        rows, cols, fuel = node
        cost = []
        for row3, col3 in self.goal_node:
            costs = abs(row3 - rows) + abs(col3 - cols) 
            cost.append(costs)
        return min(cost) * 5 

class AStarFrontier(Frontier):
    """a star frontier"""
    def __init__(self, routingGraph):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.routingGraph = routingGraph
        self.prune = set()
        self.count = 0
    def add(self, path):
        c = 0
        for tail, head, action, cost in path:
            c += cost
        c += self.routingGraph.estimated_cost_to_goal(path[-1].head)
        if path not in self.container:
            self.container.append((c, self.count, path))
            self.count += 1
            heapq.heapify(self.container)
        
    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self      
        
    def __next__(self):
        """self.container contains the whole path."""
        while len(self.container) > 0:
            the_path = heapq.heappop(self.container)[2]
            last_element = the_path[-1] 
            if last_element.head not in self.prune:
                self.prune.add(last_element.head)
                return the_path

        else:
            raise StopIteration    


def print_map(graph, frontier, solution):
    """graph is instant of the RoutingGraph.
    solution isa list of arc from the starting node to the end goal"""
    the_map = ''
    if solution:
        for index, solu in enumerate(solution):
            row, col, fuel = solu.head
            if index == 0:
                graph.map_str[row][col] = "S"
            else:
                graph.map_str[row][col] = "*"
        row, col, fuel = solu.head
        graph.map_str[row][col] = "G" 
    for pruning in frontier.prune:
        row, col, fuel = pruning
        if graph.map_str[row][col] == " ":
            graph.map_str[row][col] = "."
    for matrix in (graph.map_str):
        for column in matrix:
            the_map += str(column)
        the_map += "\n"
    print(the_map)





map_str = """\
+------------+
|         X  |
| S       X G|
|         X  |
|         X  |
|         X  |
+------------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)