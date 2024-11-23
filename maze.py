import time
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

    def generate_maze(self):
        start_x = 0
        start_y = 0
        self._break_walls_r(start_x, start_y)

    def _create_cells(self):
        for i in range(self.num_cols):           
            p = Point(self.x1,self.y1)            
            col = []
            for j in range(self.num_rows):                
                col.append(Cell(p,p,self.win.canvas))
            self._cells.append(col)
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)


    def _draw_cell(self,y, x):
        self._break_entrance_and_exit(x,y)
        x_pos = self.x1 + (x * self.cell_size_x) 
        y_pos = self.y1 + (y * self.cell_size_y)
        
        start_point = Point(x_pos, y_pos)
        end_point = Point(x_pos+self.cell_size_x,y_pos+self.cell_size_y)
        cell = self._cells[x][y]
        cell.top_left = start_point
        cell.bottom_right = end_point
        cell.draw("red")
        self._animate()

        
    def _animate(self):
        self.win.redraw() 
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self, x,y:int):
        #   print(f"x is {x} and y is {y} with {self.num_rows} and {self.num_cols}")
          if x == 0 and y == 0:
              self._cells[0][0].has_top_wall = False
          if x == self.num_cols-1 and y ==self.num_rows-1:
            #   print(f"set the bottom to false")
              self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False 

    def _break_walls_r(self, i,j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            north = (i,j-1)
            south = (i,j+1)
            east = (i+1,j)
            west = (i-1,j)
            if 0 <= north[1] < self.num_cols and 0 <= north[0] < self.num_rows:
                if not self._cells[north[0]][north[1]].visited and north not in cells_to_visit:
                    cells_to_visit.append(north)
            if 0 <= south[1] < self.num_cols and 0 <= south[0] < self.num_rows:
                if not self._cells[south[0]][south[1]].visited and south not in cells_to_visit:
                    cells_to_visit.append(south)
            if 0 <= east[0] < self.num_rows and 0 <= east[1] < self.num_cols:
                if not self._cells[east[0]][east[1]].visited and east not in cells_to_visit:
                    cells_to_visit.append(east)
            if 0 <= west[0] < self.num_rows and 0 <= west[1] < self.num_cols:
                if not self._cells[west[0]][west[1]].visited and west not in cells_to_visit:
                    cells_to_visit.append(west)
            if len(cells_to_visit) == 0:
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
        pass
            
            