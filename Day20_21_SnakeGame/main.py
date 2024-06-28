from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  #animasyonu(karelerin boşluklu bir şekilde ilerlemesini) kaldırır.

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()  # karelerin yılan gibi bir bütün şeklinde hareket etmesi için tracer kullanıldıktan sonra update metodu kullanıldı.
    time.sleep(0.1)
    snake.move()

# detect collision with food (foodla çarpışmayı tespit)
    if snake.head.distance(food) < 20:  #eğer yılan yiyeceğe 20 pikselden daha az bir yakınlıktaysa foodu yemiş kabul ederiz.foodumuz 17 piksel
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 298 or snake.head.ycor() < -295:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

# detect collision with tail
# if head collisions with any segment in the tail: trigger game_over
    for segment in snake.segments[1:]:
        # INSTEAD OF THIS WE GONNA DO SLICING LIKE ABOVE
        # if segment == snake.head:
        #    pass
        # elif snake.head.distance(segment) < 12:
        #     game_is_on = False
        #     scoreboard.game_over()
         if snake.head.distance(segment) < 12:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
