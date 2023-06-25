from turtle import Turtle, Screen
from paddle import Paddle
from movement import Movement
from screen import SetUP
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
setup = SetUP(screen)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()


move1 = Movement(r_paddle)
move2 = Movement(l_paddle)

screen.listen()
screen.onkeypress(key='Up',fun=move1.up)
screen.onkeypress(key='Down',fun=move1.down)
screen.onkeypress(key='w',fun=move2.up)
screen.onkeypress(key='s',fun=move2.down)

game_on = True
while game_on:
    screen.update()  
    ball.move()
    
    #Collision with Wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounceY()
        
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounceX()
        
        
    if ball.xcor() > 380:
        ball.setposition(0,0)
        ball.bounceX()
        ball.speed = 0.1
        scoreboard.r_point()
        
        
    if ball.xcor() < -380:
        ball.setposition(0,0)
        ball.speed = 0.1
        ball.bounceX()
        scoreboard.l_point()
    
screen.exitonclick()