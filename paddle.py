from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.goto(coordinates)
        self.color("white")
        self.setheading(90)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)
