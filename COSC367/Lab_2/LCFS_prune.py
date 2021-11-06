from search import *
import math
import heapq
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

class LCFSFrontier(Frontier):
    """Implements a frontier container appropriate for LCFS."""
    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []
        self.prune = set()
        self.count = 0
    def add(self, path):
        c = 0
        for tail, head, action, cost in path:
            c += cost
            if tail == None:
                print(f"+ {head} ", end="")
            else:
                print(f"+ {action} ", end="")

        print(f"cost = {c}")
        if path not in self.container:
            self.container.append((c, self.count, path))
            self.count += 1
            heapq.heapify(self.container)
        
        

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        while len(self.container) > 0:
            the_path = heapq.heappop(self.container)[2]
            last_element = the_path[-1] 
            if last_element.head not in self.prune:
                self.prune.add(last_element.head)
                for i in the_path:
                    if i.tail == None:
                        print(f"- {i.head}")
                    else:
                        print(f"- {i.action}")
                return the_path
            else:
                for i in the_path:
                    if i.tail == None:
                        print(f"- {i.head}!")
                    else:
                        print(f"- {i.action}!")

        else:
            raise StopIteration 
    
graph = ExplicitGraph(
    nodes={'A', 'B', 'C', 'D', 'G'},
    edge_list=[('A', 'B', 2), ('A', 'C', 3), ('B', 'D', 5),
               ('C', 'D', 5), ('D', 'G', 3),],
    starting_nodes=['A'],
    goal_nodes = {'G'},
    )
solution = next(generic_search(graph, LCFSFrontier()))
print_actions(solution)

# for arc in graph.outgoing_arcs('A'):
#     print(arc)
# print()
# for arc in graph.outgoing_arcs('B'):
#     print(arc)
# print()
# for arc in graph.outgoing_arcs('C'):
#     print(arc)