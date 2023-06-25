from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, Position) -> None:
        self.x = Position[0]
        self.y = Position[1]
        super().__init__()
        
        self.shapesize(stretch_wid=0.8,stretch_len=4)
        self.setheading(90)
        self.color('white')
        self.shape('square')
        self.penup()
        self.setposition(self.x,self.y)