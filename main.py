from turtle import Turtle ,Screen
from pad import pad
from ball import Ball
import time
from score import Score



screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("ping pong")
screen.tracer(0)
r_paddle=pad((350,0))
l_paddle=pad((-350,0))


score=Score()
ball1=Ball()
screen.listen()
screen.onkey(r_paddle.go,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.go,"w")
screen.onkey(l_paddle.down,"s")


game=True
while game:
    time.sleep(ball1.speed1)
    screen.update()
    ball1.move()

    if ball1.ycor()>280 or ball1.ycor()<-280 :
        ball1.bounce_y()
    if ball1.distance(r_paddle)<50 and ball1.xcor() >320 or ball1.distance(l_paddle) <50 and ball1.xcor()<-320:
        ball1.bounce_x()
    if ball1.xcor()> 380:
        score.l_point()
        ball1.refresh()

    if ball1.xcor()<-380:
        score.r_point()
        ball1.refresh()



screen.exitonclick()

