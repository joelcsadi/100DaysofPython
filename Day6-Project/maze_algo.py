"""
In this project, I created an algorithm that helps one escape a maze.
This project was built in the following website below,
which has an interactive user interface to show how maze escape works.

It follows a right hand wall follow approach.
The code is provided in pseudocode as the app contained its
own built-in functions.

We first find a wall and turn left to prevent an edge case of
an infinite loop since we may have no walls around us.

If there's no wall on the right, we turn right and move into it.
Else if there's no wall in front, we move forward.
Else, we just turn left so we can U-turn out.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
"""
