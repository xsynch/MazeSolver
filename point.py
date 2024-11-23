
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
        original_top_left = copy(self.top_left)
        original_bottom_right = copy(self.bottom_right)
        if self.has_top_wall:            
            line = Line(self.top_left, self.bottom_right)                                    
            line.draw(self.win,f=color) 
        if not self.has_top_wall:
            print(f"no top wall")
        if self.has_bottom_wall:
            self.top_left.y = original_top_left.y+50
            self.bottom_right.y = original_bottom_right.y+50
            
            line = Line(self.top_left, self.bottom_right)                                    
            line.draw(self.win,f=color)
        if not self.has_bottom_wall:
            print(f"no bottom wall")
        if self.has_left_wall:  
            self.top_left.y = original_top_left.y                      
            self.bottom_right.x = original_top_left.x
            self.bottom_right.y = original_bottom_right.y+50                        
            line = Line(self.top_left, self.bottom_right)                                    
            line.draw(self.win,f=color)                        
        if self.has_right_wall:
            self.bottom_right.x = original_bottom_right.x
            self.bottom_right.y = original_bottom_right.y+50
            self.top_left.x = original_bottom_right.x
            self.top_left.y = original_bottom_right.y            
            line = Line(self.top_left, self.bottom_right)                                    
            line.draw(self.win,f=color)             
            
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
        
            