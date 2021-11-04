from search import *
import math
import re
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
    def __init__(self, map_str):
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
    def starting_nodes(self):
        start = []
        for row, value in enumerate(self.map_str):
            for col, v in enumerate(value):
                found = re.search("[0-9]", self.map_str[row][col])
                if found:
                    start.append((row, col, int(found.group())))
                if self.map_str[row][col] == "S":
                    start.append((row, col, math.inf))
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
        
    
