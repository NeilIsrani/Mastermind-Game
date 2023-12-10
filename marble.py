from turtle import Turtle, Screen
class Marble:
    def __init__(self, position_x, position_y, color, size):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.position_x = position_x
        self.turtle.position_y = position_y
        self.turtle.color = color
        self.turtle.hideturtle()
        self.turtle.size = size
        self.turtle.speed(10)

    def set_color(self, color):
        self.turtle.color(color)

    def get_color(self):
        return self.turtle.color()

    def draw(self, position_x, position_y, color, size):
        self.turtle.color = color
        self.turtle.penup()
        self.turtle.speed(10)
        self.turtle.goto(position_x, position_y)
        self.turtle.visible = True
        self.turtle.is_empty = False ## if click true, is_empty is false, otherwise false
        self.turtle.fillcolor(color)
        self.turtle.begin_fill()
        self.turtle.circle(size)
        self.turtle.end_fill()
        self.turtle.pendown()
        self.turtle.speed(10)

    def draw_empty(self, position_x, position_y, size):
        #self.turtle.erase()
        self.turtle.penup()
        self.turtle.speed("fastest")
        self.turtle.goto(position_x, position_y)
        self.turtle.visible = True
        self.turtle.is_empty = True
        self.turtle.pendown()
        self.turtle.circle(size)
        

    def erase(self):
        self.turtle.clear()

    def clicked_in_region(self, x, y):
        if abs(x - self.turtle.xcor()) <= self.size * 2 and \
           abs(y - self.turtle.ycor()) <= self.size * 2:
            return True
        return False
