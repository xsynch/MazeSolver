
from tkinter import Canvas
from copy import copy 





class Point():
    def __init__(self,x:float, y:float):
        self.x = x        
        self.y = y
    
    def __repr__(self):
        return f"{__class__}({self.x},{self.y})"   
        


class Line():
    def __init__(self, start_point:Point, end_point:Point):
        self.start_point = start_point 
        self.end_point = end_point
    
    def draw(self, c:Canvas, f:str):
        c.create_line(self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y, fill=f)

    def __repr__(self):
        return f"{__class__}({self.start_point},{self.end_point})"   



class Cell():
    def __init__(self, top_left, bottom_right, win):
        self.has_left_wall = True
        self.has_right_wall = True 
        self.has_top_wall = True
        self.has_bottom_wall = True 
        self.top_left = top_left
        self.bottom_right = bottom_right        
        self.win = win 
        self.visited = False 

    def draw(self,color: str):

        top_wall = Line(Point(self.top_left.x,self.top_left.y),Point(self.bottom_right.x, self.top_left.y))
        right_wall = Line(Point(self.bottom_right.x, self.top_left.y),Point(self.bottom_right.x, self.bottom_right.y))
        bottom_wall = Line(Point(self.top_left.x, self.bottom_right.y), Point(self.bottom_right.x, self.bottom_right.y))
        left_wall = Line(Point(self.top_left.x, self.top_left.y), Point(self.top_left.x, self.bottom_right.y))
        if self.has_top_wall:                        
            top_wall.draw(self.win, f=color)
        if not self.has_top_wall:            
            top_wall.draw(self.win,f="#D9D9D9")
        if self.has_bottom_wall:                                  
            bottom_wall.draw(self.win,f=color)
        if not self.has_bottom_wall: 
            bottom_wall.draw(self.win,f="#D9D9D9")
            # print(f"no bottom wall")
        if self.has_left_wall:                                  
            left_wall.draw(self.win,f=color)
        if not self.has_left_wall:
            left_wall.draw(self.win, f="#D9D9D9")                        
        if self.has_right_wall:
            right_wall.draw(self.win,f=color)             
        if not self.has_right_wall:
            right_wall.draw(self.win,f="#D9D9D9")
            
    def __repr__(self):
        return f"{__class__}({self.top_left},{self.bottom_right},{self.win})"   
    
    def draw_move(self, to_cell, undo=False):
        halfway_from_cell_point = Point((self.top_left.x + self.bottom_right.x)/2,(self.top_left.y + self.bottom_right.y)/2)
        halfway_to_cell_point = Point((to_cell.top_left.x + to_cell.bottom_right.x)/2,(to_cell.top_left.y + to_cell.bottom_right.y)/2)
        line = Line(halfway_from_cell_point, halfway_to_cell_point)
        if not undo:            
            line.draw(self.win, "red")
        else: 
            line.draw(self.win,"gray")

    def __eq__(self, other_cell):
        return self.top_left.x == other_cell.top_left.x and self.top_left.y == other_cell.top_left.y and self.bottom_right.x == other_cell.bottom_right.x and self.bottom_right.y == other_cell.bottom_right.y
        
            