from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randrange(-280,280),random.randrange(-280,280))
