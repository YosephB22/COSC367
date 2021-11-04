from search import *
import re
import math
class RoutingGraph(Graph):
    """This is an abstract class for graphs. It cannot be directly
    instantiated. You should define a subclass of this class
    (representing a particular problem) and implement the expected
    methods."""
    def __init__(self, map_str):
        """inittializer"""
        inner_l = []
        upper_l = []
        self.matrix = map_str
        for m in self.matrix:
            if m == "\n":
                upper_l.append(inner_l)
                inner_l = []
            else:
                inner_l.append(m)
        self.matrix = upper_l
    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        row, col, cost
        return self.matrixp[row][col] == "S"
        

    def starting_nodes(self):
        """Returns a sequence of starting nodes. Often there is only one
        starting node but even then the function returns a sequence
        with one element. It can be implemented as an iterator if
        needed.
        """
        s_nodes = []
        for row_index, rows in enumerate(self.matrix):
            for col_index, cols in enumerate(rows):
                start_position = "S"
                match = re.search(r"[0-9]", cols)
                if cols == start_position:
                    s_nodes.append((row_index, col_index, math.inf))
                elif match:
                    match_int = int(match.group())
                    s_nodes.append((row_index, col_index, match_int))
        return s_nodes

    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""







map_str = """\
+-------+
|  9  XG|
|X XXX  |
| S  0FG|
+-------+
"""




graph = RoutingGraph(map_str)

print("Starting nodes:", sorted(graph.starting_nodes()))


