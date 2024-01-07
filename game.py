import pygame
import sys
from Cell import * 
from mazebuild import *
import random
from d import *
clock = pygame.time.Clock()
pygame.init()
sys.setrecursionlimit(10000)

stack = [(current_cell_x, current_cell_y)]

screen = pygame.display.set_mode((width, height))

for i in range(rows):
    row = []
    for j in range(cols):
        cell = Cell(j, i, screen,maze_wall_size) 
        row.append(cell)
    maze.append(row)

current_cell = maze[0][0]

start = (0, 0) 
end = (cols - 1, rows - 1) 

fps = 120
bfs_search = BFS(maze, start, end)
running = True

maze_generation_complete = False
maze_finding_complete = False
real_shortest_path = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255)) 

    if not maze_generation_complete:
        if len(stack)==0:
            maze_generation_complete = True
            fps = 30
            continue
           
        current_cell.visit = True
        current_cell.draw_current_cell()
        neighbors = current_cell.get_unvisited_neighbors(maze)
        if neighbors:
            next_cell = random.choice(neighbors)
            if next_cell:
                next_cell.visit = True
                stack.append(current_cell)
                current_cell.remove_walls(next_cell)
                current_cell = next_cell
        else:
            current_cell = stack.pop()
    
    for row in maze:
        for cell in row:
            cell.draw()
    
    if maze_generation_complete and not maze_finding_complete:
        shortest_path = bfs_search.find_shortest_path()
        if shortest_path:
            
            maze_finding_complete = True
        
    bfs_search.draw_shortest_path()
    
    clock.tick(fps)
    pygame.display.flip()  
   

pygame.quit()
sys.exit()