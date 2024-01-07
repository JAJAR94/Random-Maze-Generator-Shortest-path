class Node:
    def __init__(self, pos, parent):
        self.x = pos[0]
        self.y = pos[1]
        self.parent = parent

    def get_position(self):
        return (self.x, self.y)
    
    def get_parent(self):
        return self.parent

class Queue:
    def __init__(self):
        self.Queue = []

    def size(self):
        return len(self.Queue)

    def append(self, node):
        self.Queue.append(node)

    def pop(self):
        return self.Queue.pop(0)

    def get_node_position(self):
        node = self.Queue[0]
        return node.get_position() 

class BFS:
    def __init__(self, maze,start,end):
        self.maze = maze
        self.start = start
        self.end = end
        self.frontier = Queue()
        self.explored = Queue()
        self.shortest_path = []
        node = Node(pos=start, parent=None)
        self.frontier.append(node)

    def find_shortest_path(self):
    
        current_node = self.frontier.pop()
        print(current_node.x,current_node.y)
        self.draw_path_maze()
        if current_node.get_position() == self.end:
            self.back_track(current_node)
            return True

        self.explored.append(current_node)
            
        for each_cell in self.check_move(current_node):
            new_node = Node(pos=(each_cell.x, each_cell.y), parent=current_node)

            if not self.is_explored_or_frontier(new_node):
                

                self.frontier.append(new_node)
             

    def draw_path_maze(self):
        for node in self.explored.Queue:
            x, y = node.get_position()
 
            if 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze):
                self.maze[y][x].draw_path() 

    def draw_shortest_path(self):
        for node in self.shortest_path:
            x, y = node.get_position()
            if 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze):
                self.maze[y][x].draw_path() 


    def is_explored_or_frontier(self, new_node):
        for node in self.frontier.Queue + self.explored.Queue:
            if node.get_position() == new_node.get_position():
                return True
        return False
        

    def back_track(self, node):
        current_node = node
        while current_node is not None:
            self.shortest_path.append(current_node)
            current_node = current_node.get_parent()
        
    

    def check_move(self,node):
        next_moves = []
        directions = {
        'top': (0, -1),   
        'right': (1, 0),   
        'left': (-1, 0), 
        'bottom': (0, 1)   
        }

        x, y = node.get_position()

        for direction, (dx, dy) in directions.items():
            if not getattr(self.maze[y][x], direction):  
                new_x, new_y = x + dx, y + dy
                if 0 <= new_y < len(self.maze) and 0 <= new_x < len(self.maze[0]):
                    next_moves.append(self.maze[new_y][new_x])

        return next_moves



        


