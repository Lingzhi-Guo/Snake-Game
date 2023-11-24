from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_new_body(position)

    def add_new_body(self, position):
        body = Turtle(shape="square")
        body.color("green")
        body.penup()
        body.setposition(position)
        self.snake_body.append(body)

    def extend(self):
        self.add_new_body(self.snake_body[-1].position())

    def move(self):
        for num in range(len(self.snake_body) - 1, -1, -1):
            if num == 0:
                self.snake_body[0].forward(20)
            else:
                self.snake_body[num].goto(self.snake_body[num - 1].position())

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def reset(self):
        for body in self.snake_body:
            body.goto(x=1000, y=-1000)
        self.snake_body.clear()
        self.create_snake()