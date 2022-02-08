from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cor=20
        self.y_cor =20
        self.goto(0,0)
        self.speed1=0.1

    def move(self):
        newx=self.xcor()+self.x_cor
        newy=self.ycor()+self.y_cor
        self.goto(newx,newy)
    def bounce_y(self):
        self.y_cor*=-1
    def bounce_x(self):
        self.x_cor*=-1
        self.speed1*=0.9
    def refresh(self):
        self.goto(0,0)
        self.speed1=0.1


