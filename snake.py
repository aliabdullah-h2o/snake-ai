from config import *
from copy import deepcopy
import random

class Food:
    def __init__(self, snake):
        pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)]
        while pos in snake.body_pos:
            pos = [random.randint(0, COLS - 1), random.randint(0, ROWS - 1)] 
        self.pos = pos
    
    def update_loc(self, snake):
        pos = [random.randint(0, COLS -1), random.randint(0, ROWS-1)] 
        while (pos in snake.body_pos) and (pos!=self.pos):
            pos = [random.randint(0, COLS -1), random.randint(0, ROWS-1)] 
        self.pos = pos

class Snake:
    def __init__(self):
        self.body_pos = [[0, 0]]
    
    def move(self, direction):
        body_pos_cp = deepcopy(self.body_pos)
        for i in range(1, len(self.body_pos)):
            self.body_pos[i][0] = body_pos_cp[i-1][0] 
            self.body_pos[i][1] = body_pos_cp[i-1][1]

        self.body_pos[0][0] += direction[0]
        self.body_pos[0][1] += direction[1]
    
    def eat(self, food):
        food.update_loc(self)
        self.body_pos.append([None,None])
    
    def is_alive(self):
        if self.body_pos[0] in self.body_pos[1:]:
            return False
        return True 
    
    def check_food_collision(self, food):
        if self.body_pos[0] == food.pos:
            self.eat(food)