from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()
    if snake.snake_body[0].distance(food) <= 17:
        food.change_position()
        snake.extend()
        score.change_score()

    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -300 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280:
        score.reset()
        snake.reset()

    for body in snake.snake_body[1:]:
        if snake.snake_body[0].distance(body) < 10:
            score.reset()
            snake.reset()

score.end_game()

screen.exitonclick()