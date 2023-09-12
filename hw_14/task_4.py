# assume 4 options for orientation relative to (0,0):
#    "up" (+y), "down" (-y), "left" (-x), "right" (+x)
class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps):
        if self.orientation == "up":
            self.position_y += steps
        elif self.orientation == "down":
            self.position_y -= steps
        elif self.orientation == "left":
            self.position_x -= steps
        else:
            self.position_x += steps

# "right" turn the robot clockwise 90 degrees, "left" turn it counter-clockwise
    def turn(self, direction):
        if direction == "right":
            turn = 1
        elif direction == "left":
            turn = -1

        turn_sequence_r = ("up", "right", "down", "left")
        index = turn_sequence_r.index(self.orientation)

        new_index = (index + turn) % len(turn_sequence_r)
        self.orientation = turn_sequence_r[new_index]

    def display_position(self):
        position = (self.position_x, self.position_y)
        print(position)


robot = Robot("up", 0, 0)

robot.turn("left")
robot.move(3)
robot.display_position()
