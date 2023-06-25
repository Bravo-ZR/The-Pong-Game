from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.1
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        time.sleep(self.speed)
        
        
    def bounceY(self):
        self.y_move *= -1
        
        
    def bounceX(self):
        self.x_move *= -1
        self.speed *= 0.9
    