from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.names = []
        self.create_snake()
        self.head = self.names[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_name = Turtle("square")
        new_name.color("white")
        new_name.penup()
        new_name.goto(position)
        self.names.append(new_name)

    def reset(self):
        for name in self.names:
            name.goto(1000, 1000)
        self.names.clear()
        self.create_snake()
        self.head = self.names[0]

    def extend(self):
        self.add_segment(self.names[-1].position())

    def move(self):
        for name_num in range(len(self.names) - 1, 0, -1):
            new_x = self.names[name_num - 1].xcor()
            new_y = self.names[name_num - 1].ycor()
            self.names[name_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



