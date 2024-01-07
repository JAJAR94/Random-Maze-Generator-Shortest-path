import pygame

class Cell:
    def __init__(self,x,y,screen,size):
        self.screen = screen
        self.x = x
        self.y = y
        self.top = True
        self.bottom = True
        self.right = True
        self.left = True
        self.visit = False
        self.cell_width = size
        self.cell_height = size
        self.top_left = (self.x * self.cell_width, self.y * self.cell_height)
        self.top_right = (self.x * self.cell_width + self.cell_width, self.y * self.cell_height)
        self.bottom_left = (self.x * self.cell_width, self.y * self.cell_height + self.cell_height)
        self.bottom_right = (self.x * self.cell_width + self.cell_width, self.y * self.cell_height + self.cell_height)


    def draw_current_cell(self):
        rect = pygame.Rect(self.top_left, (self.cell_width, self.cell_height))
        pygame.draw.rect(self.screen, pygame.Color('red'), rect)


    def draw_path(self):
        center_x = self.top_left[0] + self.cell_width // 2
        center_y = self.top_left[1] + self.cell_height // 2
        radius = int(min(self.cell_width, self.cell_height) * 0.4)
        pygame.draw.circle(self.screen, pygame.Color('red'), (center_x, center_y), radius)


    def draw(self):
    
        if not self.visit:
            rect = pygame.Rect(self.top_left, (self.cell_width, self.cell_height))
            pygame.draw.rect(self.screen, pygame.Color('blue'), rect)
        
        if self.top:
            pygame.draw.line(self.screen, pygame.Color('black'), self.top_left, self.top_right)
        if self.bottom:
            pygame.draw.line(self.screen, pygame.Color('black'), self.bottom_left, self.bottom_right)
        if self.left:
            pygame.draw.line(self.screen, pygame.Color('black'), self.top_left, self.bottom_left)
        if self.right:
            pygame.draw.line(self.screen, pygame.Color('black'), self.top_right, self.bottom_right)

    def get_unvisited_neighbors(self, maze):
        neighbors = []
        x, y = self.x, self.y
        directions = [
        (x - 1, y),  
        (x + 1, y),  
        (x, y - 1),  
        (x, y + 1)  
        ]

   
        for nx, ny in directions:
     
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and not maze[ny][nx].visit:
           
                neighbors.append(maze[ny][nx])

        return neighbors


    def remove_walls(self, next_cell):
        dx = self.x - next_cell.x
        dy = self.y - next_cell.y
        if dx == 1:  
            self.left = False
            next_cell.right = False
        elif dx == -1: 
            self.right = False
            next_cell.left = False
        if dy == 1: 
            self.top = False
            next_cell.bottom = False
        elif dy == -1:  
            self.bottom = False
            next_cell.top = False



