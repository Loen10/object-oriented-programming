class Vehicle:
    pass

bug = Vehicle()
turtle = Vehicle()
rover = Vehicle()

bug.color = "yellow"
bug.num_wheels = 4
bug.speed = 1

turtle.color = "green"
turtle.num_wheels = 2
turtle.speed = 5

rover.color = "purple"
rover.num_wheels = 4
rover.speed = 25

print("The bug's speed is", bug.speed, "and it's color is", bug.color)
print("The turtle's speed is", turtle.speed, "and it's color is", turtle.color)
print("The rover's speed is", rover.speed, "and it's color is", rover.color)