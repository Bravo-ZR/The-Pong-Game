from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.write(self.l_score, align='Center', font=('Courier', 70, 'normal'))
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.goto(-100,200)
        self.write(self.l_score, align='Center', font=('Courier', 70, 'normal'))
        self.goto(100,200)
        self.write(self.r_score, align='Center', font=('Courier', 70, 'normal'))
        
        
    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
        
        
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
        