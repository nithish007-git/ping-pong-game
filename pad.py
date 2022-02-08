from turtle import Turtle

class pad(Turtle):




    def __init__(self,posti):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(posti)

    def go(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)




