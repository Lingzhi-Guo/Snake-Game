from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 230)
        with open("high_score.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.highscore}", move=False, align="center", font=("Arial", 30, "normal"))

    def change_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.highscore}", move=False, align="center", font=("Arial", 30, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.highscore}", move=False, align="center", font=("Arial", 30, "normal"))
