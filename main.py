
from point import *
from window import *
from maze import *





        


    


def main():
    # win = Window(1024,768)
    line1 = Line(Point(15,25),Point(600, 25))
    # print(line1)
    # win.draw_line(line1, "red")
    # line2 = Line(Point(15,25),Point(200, 25))
    # win.draw_line(line2, "blue")

    # cell = Cell(Point(15,25),Point(600,25),win.canvas)
    # cell.has_bottom_wall = False
    # cell.has_left_wall = False
    # cell.has_top_wall = False 
    # cell.draw("red")
    # # print(cell)

    # cell2 = Cell(Point(30,50),Point(60,100),win.canvas)
    # cell2.draw("blue")

    # cell2.draw_move(cell)

    win = Window(1024,768)
    num_cols = 12
    num_rows = 12
    margin = 50
    cell_size_x = (800 - 2 * margin) / num_cols
    cell_size_y = (600 - 2 * margin) / num_rows
    m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y,win)
    m1.generate_maze()
    print(m1.solve())
    
    # print(f"The number of maze cells is: {len(m1._cells)}")
            

    win.wait_for_close()



if __name__ == "__main__":
    main()