import pygame
from colors import Colors

class Grid:
     def __init__(self):
          self.num_rows = 20
          self.num_col = 10
          self.cell_size = 30
          #colors
          self.colors = Colors.get_cell_colors()


        #list comprehension, a short way to make a 2D list
          self.grid = [[0 for j in range(self.num_col)] for i in range(self.num_rows)]

     def print_grid(self):
          for row in range(self.num_rows):
               for colum in range(self.num_col):
                    print(self.grid[row][colum], end=" ")
               print()
     
     def draw(self, screen):
          for row in range(self.num_rows):
               for col in range(self.num_col):
                    cell_value = self.grid[row][col]
                    cell_rect = pygame.Rect(col*self.cell_size+1, row*self.cell_size+1, self.cell_size-1, self.cell_size-1)
                    pygame.draw.rect(screen, self.colors[cell_value], cell_rect)