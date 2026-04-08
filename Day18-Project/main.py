import colorgram
from turtle import Turtle, Screen 
import random
# colors = colorgram.extract("img.jpg", 20)
# initial_colors_list = []
# for color in colors:
#     # print(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r,g,b)
#     initial_colors_list.append(rgb_tuple)

selected_colors = [
    (226, 147, 98),
    (28, 102, 177),
    (161, 56, 90),
    (148, 79, 51),
    (225, 61, 96),
    (113, 174, 215),
    (244, 227, 95),
    (173, 20, 41),
    (233, 79, 51),
    (224, 126, 156),
    (118, 184, 130),
    (11, 172, 207),
    (165, 151, 25),
    (13, 58, 148),
    (83, 37, 23),
    (128, 37, 27)
]
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.hideturtle()
tim.pu()
tim.setheading(225)
tim.forward(325)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")

# 100 dots of 20 radius each with random colors 
for dot_count in range(1,number_of_dots+1):
    random_color=random.choice(selected_colors)
    tim.dot(20, random_color)
    tim.forward(50)

    # Restart the row
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()

