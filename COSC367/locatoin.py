from search import *
import math
class LocationGraph(Graph):
    """This is a concrete subclass of Graph where vertices and edges
     are explicitly enumerated. Objects of this type are useful for
     testing graph algorithms."""

    def __init__(self, nodes, locations, edges, starting_nodes, goal_nodes, estimates=None):
        self.nodes = nodes    
        self.locations = locations
        self.edges = edges
        self.edges = self.bidirectional_edges(edges)
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
        self.estimates = estimates

    def starting_nodes(self):
        """Returns a sequence of starting nodes."""
        return self._starting_nodes

    def is_goal(self, node):
        """Returns true if the given node is a goal node."""
        return node in self.goal_nodes

    def bidirectional_edges(self, edges):
        new_edge = set()
        for (tail, head) in self.edges:
            new_edge.add((tail, head))
            new_edge.add((head, tail))
        return new_edge 
            
        
    def outgoing_arcs(self, node):
        """Returns a sequence of Arc objects that go out from the given
        node. The action string is automatically generated.
        """
        location = self.locations
        arcs = set()
        for edge in self.edges:
            if len(edge) == 2:  # if no cost is specified
                tail, head = edge
                x_difference = (location[head][0] - location[tail][0]) ** 2
                y_difference = (location[head][1] - location[tail][1]) ** 2
                cost = math.sqrt(x_difference + y_difference)  
            else:
                tail, head, cost = edge
            if tail == node:
                arcs.add(Arc(tail, head, str(tail) + '->' + str(head), cost))
        arc = sorted(arcs)
        return arc