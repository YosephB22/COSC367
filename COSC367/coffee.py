
from collections import deque
from search import *
BLANK = "BRICK"
# a state is a triple ((x,y),c) where
#   robot is at position (x,y) where the bottom left location is (0,0)
#   Boolean c specified whether the robot has coffee
class SlidingPuzzleGraph(Graph):
    def start_node(self):
        """returns the start node"""
        return ((3,2),False)
    
    def is_goal(self,node):
        """returns True when node is a goal node"""
        return node == ((3,4),True)
    
    def outgoing_arcs(self,node):
        """returns a list of the neighbors of node.
           note that the neighbors are arcs.
        """    
        ((x,y),c) = node
        arc = []
        for (dx,dy) in [(-1,0),(1,0),(0,1),(0,-1)]:
            for pos in (x+dx, y+dy):
                if self.legal(pos):
                    if self.at_coffee(pos):
                        arcs.append(Arc(node, (pos,True), action, 1))   
                    else:
                        arcs.append(Arc(node, (pos,c), action, 1))
        return arcs
    def legal(self,pos):
        (x,y) = pos
        """returns True when position (x,y) is a legal position"""
        return x>=0 and x<9 and y>=0 and y<6 and (
            y in [0,5] if x==1 else
            (x==0 or x>5 if y==3 else
            (x,y) != (5,4)))
    
    def at_coffee(self,pos):
        """returns True when pos is a locoation of a coffee shop"""
        return pos in [(0,0),(4,0),(7,4)]
    
class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = deque()
    def add(self, path):
        return self.container.append(path) 

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0: #not empty
            return self.container.popleft() #selecting the last element
        else:
            raise StopIteration   # don't change this one
        
class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = deque()
    def add(self, path):
        return self.container.append(path) 

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0: #not empty
            return self.container.popleft() #selecting the last element
        else:
            raise StopIteration   # don't change this one

m = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    [' ', 'BRICK', ' ', 'G', ' ', 'BRICK', ' ', 'C3', ' '], 
    [' ', 'BRICK', 'BRICK', 'BRICK', 'BRICK', 'BRICK', ' ', ' ', ' '], 
    [' ', 'BRICK', ' ', 'S', ' ', ' ', ' ', ' ', ' '], 
    [' ', 'BRICK', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
    ['C1', ' ', ' ', ' ', 'C2', ' ', ' ', ' ', ' ']]
from search import generic_search, print_actions
graph = SlidingPuzzleGraph(m)
solutions = generic_search(graph, BFSFrontier())
print_actions(next(solutions))