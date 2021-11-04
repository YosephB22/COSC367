row = 3
column = 3
class Tree:
    def __init__(self, grid):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.cost = 0
        self.brick = "BRICK"
        self.grid = grid
        #the root is at grid 3 X 3
        self.root = self.grid[3][3]
        print(self.root)
    def add_up(self):
        global row, column
        self.root = self
        new_node = self.grid[row - 1][column]
        if self.up is None:
            if self.grid[row - 1][column] != self.brick:
                self.up = Tree(self.grid)
                row -= 1
            return self.up
    def add_down(self):
        global row, column
        self.root = self
        if self.down is None:
            new_node = self.grid[row + 1][column]
            if self.grid[row + 1][column] != brick:
                self.down = Tree(self.grid)
                row += 1
            return self.down  
    def add_left(self):
        global row, column
        self.root = self
        new_node = self.grid[row][column - 1]
        if self.left is None:
            if self.grid[row][column - 1] != self.brick:
                self.left = Tree(self.grid)
                self.column = column - 1
            return self.left        
    def add_right(self):
        global row, column
        self.root = self
        if self.right is None:
            new_node = self.grid[row][column + 1]
            if self.grid[row][column + 1] != self.brick:
                self.right = Tree(self.grid)
                column = column + 1
            return self.right

goal = "G"
def traverse(matrix, root):
    root = Tree(matrix)
    if a_tree.grid[row][column] != goal:
        traverse(matrix)
    while a_tree.grid[row][column] != goal:
        print(a_tree.grid[row][column])
        a_tree.add_down()
        a_tree.add_right()
        a_tree.add_left()
        a_tree.add_up()
    return a_tree.grid[row][column]
    
brick = "BRICK"
matrix = [[" "] * 9 for i in range(6)]
matrix[1][1], matrix[1][5], matrix[3][1], matrix[4][1] = brick, brick, brick, brick
matrix[1][3], matrix[1][7], matrix[5][0], matrix[5][4], matrix[3][3] = "G", "C3", "C1", "C2", "S"
for index, fill in enumerate(matrix[2]):
    if index >= 1 and index <= 5:
        matrix[2][index] = brick
matrix[1][5] = brick   
    
print(traverse(matrix))
