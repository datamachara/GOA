import turtle

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("skyblue")

# Create a turtle object
castle = turtle.Turtle()
castle.speed(5)  # Set the speed of the turtle

# Function to draw a rectangle (used for walls)
def draw_rectangle(width, height):
    for _ in range(2):
        castle.forward(width)
        castle.left(90)
        castle.forward(height)
        castle.left(90)

# Function to draw a circle (used for round windows)
def draw_circle(radius):
    castle.circle(radius)

# Function to draw a triangle roof
def draw_roof(base_width):
    castle.forward(base_width / 2)
    castle.left(120)
    castle.forward(base_width)
    castle.left(120)
    castle.forward(base_width)
    castle.left(120)
    castle.forward(base_width / 2)

# Function to draw a flag on top of a tower
def draw_flag():
    castle.left(90)
    castle.forward(50)
    castle.right(90)
    castle.forward(20)
    castle.right(135)
    castle.forward(28.28)  # Diagonal of a square (flag)
    castle.right(90)
    castle.forward(28.28)  # Diagonal of a square (flag)
    castle.right(135)
    castle.penup()
    castle.backward(20)
    castle.pendown()

# Function to draw a tower with roof, flag, and windows
def draw_tower(base_width, height, window_radius):
    draw_rectangle(base_width, height)  # Draw tower base
    
    castle.penup()
    castle.left(90)
    castle.forward(height)  # Move to the top of the tower
    castle.right(90)
    
    draw_roof(base_width)  # Draw triangular roof
    draw_flag()  # Draw flag at the top of the roof

    # Move to the position for windows
    castle.right(90)
    castle.penup()
    castle.forward(height / 2)
    castle.left(90)
    castle.forward(base_width / 2)
    castle.pendown()

    draw_circle(window_radius)  # Draw round window

    castle.penup()
    castle.backward(base_width / 2)
    castle.left(90)
    castle.forward(height / 2)
    castle.right(90)
    castle.pendown()

# Draw the left tower
castle.penup()
castle.goto(-250, -200)  # Starting position of the left tower
castle.pendown()
draw_tower(100, 200, 20)  # Tower width=100, height=200, window radius=20

# Draw the middle (tallest) tower
castle.penup()
castle.goto(-50, -200)  # Starting position of the middle tower
castle.pendown()
draw_tower(120, 300, 30)  # Tower width=120, height=300, window radius=30

# Draw the right tower
castle.penup()
castle.goto(200, -200)  # Starting position of the right tower
castle.pendown()
draw_tower(100, 200, 20)  # Tower width=100, height=200, window radius=20

# Draw the wall connecting the towers
castle.penup()
castle.goto(-250, -200)
castle.pendown()
draw_rectangle(550, 100)  # Wall width=550, height=100

# Hide the turtle
castle.hideturtle()

# Keep the window open
window.mainloop()


