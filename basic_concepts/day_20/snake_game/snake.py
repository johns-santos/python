from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
                
    def create_snake(self):
    # Create snake body out of  3 squares - easiest way use tuple and forloop
        for position in STARTING_POSITIONS:
            self.add_segment(position)
                      
    def add_segment(self, position):
        new_segment = Turtle("square")   
        new_segment.color("magenta")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def snake_reset(self):
        #Send dead snake segments to off screen location
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        # initialize snake - at center of screen
        self.create_snake()
        self.head = self.segments[0]

    def extend_snake(self):
        # Add segment to end of segments list
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # If heading is not DOWN(270) then change to UP(90)
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)