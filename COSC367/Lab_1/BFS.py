from search import *
from collections import deque
class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = deque()
    def add(self, path):
        #raise NotImplementedError # FIX THIS
        for p in path:
            if p.tail != None:
                print(f"+ {p.action} cost = {p.cost}")
            else:
                print(f"+ {p.head} cost = {p.cost}")

        return self.container.append(path) 

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0: #not empty
            #raise NotImplementedError # FIX THIS return something instead
            v = self.container.copy()
        
            v_pop = v.popleft()
            for l in v_pop:
                if l.tail != None:
                    print(f"- {l.action}")
                else:
                    print(f"- {l.head}")
            return self.container.popleft() #selecting the last element
        else:
            raise StopIteration   # don't change this one
        

graph = ExplicitGraph(
    nodes={'G', 'B', 'C', 'A'},
    edge_list=[('B', 'G'), ('C', 'A'), ('G','A'), ('C','G')],
    starting_nodes=['C'],
    goal_nodes={'B'},
    )
solutions = generic_search(graph, BFSFrontier())
solution = next(solutions, None)
print_actions(solution)