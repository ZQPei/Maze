import numpy as np
import os
import time
import cv2

class Point:
    def __init__(self, x,y,d=None):
        self.x = x
        self.y = y
        self.dirs = [1,2,3,4]
        if d:
            self.dirs.remove((d+1)%4+1)
        self.d = self.dirs[0]

    @property
    def pos(self):
        return self.x,self.y

    def get_coord(self, d):
        x = self.x+(3-d) if d%2==0 else self.x
        y = self.y+(2-d) if d%2 else self.y
        return x,y
        
    def get_dir(self, maze):
        d = 0
        while self.dirs:
            d = self.dirs.pop(0)
            x,y = self.get_coord(d)
            if maze.get_val(x,y) :
                continue
            else:
                break
        else:
            d = 0
        self.d = d
        return d

    def __repr__(self):
        return "x={},y={},dirs={}".format(self.x,self.y,self.dirs)

class Maze:
    def __init__(self, maze_str):
        maze_list = [[int(i) for i in x.strip().split(' ')] for x in maze_str]
        self.maze = np.array(maze_list)
        self.height, self.width = self.shape = self.maze.shape
        
    def get_val(self,x,y):
        return self.maze[x,y]

    def set_value(self, x,y,val):
        self.maze[x,y] = val

class Solution:
    def __init__(self, maze_str):
        self.maze = Maze(maze_str)
        self.start = (1,1)
        self.end   = (8,8)
        self.path = []

    def print_maze(self):
        os.system("cls")
        print(self.maze.maze)

        N = 20
        self.board = self.maze.maze.astype(np.uint8)
        self.board[self.board==0] = 255
        self.board[self.board==1] = 0
        self.board[self.board==2] = 180
        self.board[self.board==3] = 50


        self.board = self.board.repeat(N,0).repeat(N,1)
        cv2.imshow("maze",self.board)
        cv2.waitKey(1)
        # time.sleep(1)

    def solve(self):
        self.path.append(Point(*self.start))
        self.maze.set_value(*self.start, 2)
        self.print_maze()
        while True:
            cur = self.path[-1]
            if cur.pos == self.end:
                print("done")
                break
            d = cur.get_dir(self.maze)
            if d:
                cur = Point(*cur.get_coord(d),d)
                self.maze.set_value(*cur.pos, 2)
                self.print_maze()
                self.path.append(cur)
            else:
                cur = self.path.pop()
                self.maze.set_value(*cur.pos, 3)
                self.print_maze()



def main():
    # OLD_MAZE  =  '''1 1 1 1 1 1 1 
    #                 1 0 0 0 0 0 1 
    #                 1 1 0 1 1 1 1 
    #                 1 0 0 1 1 0 1 
    #                 1 0 1 0 0 0 1 
    #                 1 0 0 0 1 0 1 
    #                 1 1 1 1 1 1 1''' 
    with open("maze.txt",'r') as foo:
        MAZE = foo.readlines()
    print(MAZE)
    Solution(MAZE).solve()
    

if __name__ == '__main__':
    main()