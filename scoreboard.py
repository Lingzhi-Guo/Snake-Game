from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 230)
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Arial", 30, "normal"))

    def change_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Arial", 30, "normal"))

    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.pencolor("red")
        self.write(f"GAME OVER\nSCORE: {self.score}", move=False, align="center", font=("Arial", 30, "normal"))