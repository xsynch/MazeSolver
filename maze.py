import time
from turtle import undo
from point import Point, Line, Cell 
import random 


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            seed = None 
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win 
        self._cells = []        
        self._create_cells()
        self._break_entrance_and_exit()

    def generate_maze(self):
        start_x = 0
        start_y = 0
        self._break_walls_r(start_x, start_y)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols): 
         
            # p = Point(self.x1,self.y1)            
            col = []
            for j in range(self.num_rows):
                x_pos = self.x1 + (i * self.cell_size_x) 
                y_pos = self.y1 + (j * self.cell_size_y)
                start_point = Point(x_pos, y_pos)
                end_point = Point(x_pos+self.cell_size_x,y_pos+self.cell_size_y)                 
                col.append(Cell(start_point,end_point,self.win.canvas))
            self._cells.append(col)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self,x, y):
        
        # x_pos = self.x1 + (x * self.cell_size_x) 
        # y_pos = self.y1 + (y * self.cell_size_y)
        
        # start_point = Point(x_pos, y_pos)
        # end_point = Point(x_pos+self.cell_size_x,y_pos+self.cell_size_y)
        # cell = self._cells[x][y]
        # cell.top_left = start_point
        # cell.bottom_right = end_point
        # cell.draw("red")
        self._cells[x][y].draw("red")
        self._animate()

        
    def _animate(self):
        self.win.redraw() 
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
                
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False 
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i,j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            north = (i,j-1)
            south = (i,j+1)
            east = (i+1,j)
            west = (i-1,j)
            
            if j > 0 and not self._cells[north[0]][north[1]].visited:
                    cells_to_visit.append(north)            
            if j < self.num_rows - 1 and not self._cells[south[0]][south[1]].visited:
                    cells_to_visit.append(south)            
            if i < self.num_cols - 1 and not self._cells[east[0]][east[1]].visited:
                    cells_to_visit.append(east)            
            if i > 0 and not self._cells[west[0]][west[1]].visited:
                    cells_to_visit.append(west)
            if len(cells_to_visit) == 0:
                self._draw_cell(i,j)
                return 
            else: 
                next_visit = random.choice(cells_to_visit)
                if next_visit == north:
                    self._cells[i][j].has_top_wall = False 
                    self._cells[next_visit[0]][next_visit[1]].has_bottom_wall = False 

                if next_visit == south:
                    self._cells[i][j].has_bottom_wall = False 
                    self._cells[next_visit[0]][next_visit[1]].has_top_wall = False

                if next_visit == east:
                    self._cells[i][j].has_right_wall = False 
                    self._cells[next_visit[0]][next_visit[1]].has_left_wall = False

                if next_visit == west:
                    self._cells[i][j].has_left_wall = False 
                    self._cells[next_visit[0]][next_visit[1]].has_right_wall = False

                self._break_walls_r(next_visit[0],next_visit[1])


    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False                

    def solve(self):
        return self._solve_r(0,0) 
    
    def _solve_r(self,x,y):
        
                
        self._animate()
        self._cells[x][y].visited = True 
        if x == self.num_cols -1 and y == self.num_rows -1:
             return True 
        directions = [(x,y-1),(x,y+1),(x+1,y),(x-1,y)]
        for dir in directions:
             
             if 0 <= dir[0] < self.num_cols and 0 <= dir[1] < self.num_rows and not self._cells[dir[0]][dir[1]].visited:
                
                if dir[1] == y+1 and dir[0] == x and not self._cells[x][y].has_bottom_wall:
                    self._cells[x][y].draw_move(self._cells[dir[0]][dir[1]])
                    if not self._solve_r(dir[0],dir[1]):
                         self._cells[x][y].draw_move(self._cells[dir[0]][dir[1]],undo=True)
                    else:
                         return True 
                
                elif dir[1] == y-1 and dir[0] == x and not self._cells[x][y].has_top_wall:
                    self._cells[x][y].draw_move(self._cells[dir[0]][dir[1]])
                    if not self._solve_r(dir[0],dir[1]):
                         self._cells[x][y].draw_move(self._cells[dir[0]][dir[1]],undo=True)
                    else:
                         return True 
                    
                elif dir[0] == x+1 and dir[1] == y and not self._cells[x][y].has_right_wall:
                    self._cells[x][y].draw_move(self._cells[dir[0]][dir[1]])
                    if not self._solve_r(dir[0],dir[1]):
                         self._cells[x][y].draw_move(self._cells[dir[0]][dir[1]],undo=True)
                    else:
                         return True 
                elif dir[0] == x-1 and dir[1] == y and not self._cells[x][y].has_left_wall:
                    self._cells[x][y].draw_move(self._cells[dir[0]][dir[1]])
                    if not self._solve_r(dir[0],dir[1]):
                         self._cells[x][y].draw_move(self._cells[dir[0]][dir[1]],undo=True)
                    else:
                         return True 

        

        return False
            