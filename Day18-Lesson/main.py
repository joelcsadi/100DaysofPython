from turtle import Turtle, Screen
import random

# Drawing a square with turtle graphics
tim = Turtle()
tim.shape("turtle")
tim.color("darkGreen") 
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)




# Drawing a dashed line with turtle graphics
# for i in range(50):
#     tim.pendown()
#     tim.forward(4)
#     tim.penup()
#     tim.forward(4) 

# Drawing shapes around shapes
# colors_list = ["firebrick","dark green","indigo", "maroon","yellow","dark olive green", "medium blue", "gray"]

# sides = 3
# angle = 360 / sides
# while sides < 11:
#     tim.color(random.choice(colors_list))
#     for side in range(sides):
#         tim.forward(50)
#         tim.right(angle)
#     sides += 1
#     angle = 360 / sides

# Random Walk
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
    
screen = Screen()
# screen.colormode(255) 
# tim.width(15)
# tim.speed("fastest")
# walk_directions = [0, 90, 180, 270]
# for _ in range(1000):
#     rgb = random_color()
#     tim.pencolor(rgb)
#     angle = random.choice(walk_directions)
#     tim.setheading(angle)
#     tim.forward(30)

# Spirograph
angle = 0
screen.colormode(255)
tim.speed("fastest")

def draw_spirograph(gap_size):
    for _ in range(int(360/ gap_size)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(10)


screen.exitonclick()
