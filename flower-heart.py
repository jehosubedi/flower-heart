import turtle

def draw_heart(turtle_obj, size, color):
    """Draws a heart shape of given size and color."""
    turtle_obj.color(color)
    turtle_obj.begin_fill()
    turtle_obj.left(50)
    turtle_obj.forward(size)
    turtle_obj.circle(size * 0.5, 200)
    turtle_obj.right(140)
    turtle_obj.circle(size * 0.5, 200)
    turtle_obj.forward(size)
    turtle_obj.end_fill()
    turtle_obj.left(50)

def draw_flower_with_longer_petals():
    """Draws a flower with longer heart-shaped petals and a heart center."""
    # Setup screen and turtle
    screen = turtle.Screen()
    screen.bgcolor("black")
    flower = turtle.Turtle()
    flower.speed(0)
    
    num_petals = 12  # Number of heart-shaped petals
    petal_size = 150  # Size of each heart (longer petals)
    petal_colors = ["#fb6f92", "#ff8fab", "#ffb3c6", "#ffc2d1"]  # Colors for the petals
    
    # Draw the petals first
    for i in range(num_petals):
        flower.penup()
        flower.goto(0, 0)
        flower.pendown()
        flower.setheading(360 / num_petals * i)  # Rotate for the next petal
        draw_heart(flower, petal_size, petal_colors[i % len(petal_colors)])
    
    # # Draw the heart-shaped center
    flower.penup()
    flower.goto(12, -29)  # Adjust position for the center heart
    flower.setheading(0)
    flower.pendown()
    draw_heart(flower, 60, "white")  # Yellow heart at the center

    # Draw the stem
    flower.penup()
    flower.goto(0, -30)
    flower.setheading(270)
    flower.color("green")
    flower.pensize(8)
    flower.pendown()
    flower.forward(200)

    # Add leaves
    for angle in [-755, 80]:  # Angles for left and right leaves
        flower.penup()
        flower.goto(0, -120)
        flower.setheading(angle)
        flower.pendown()
        flower.color("green")
        flower.begin_fill()
        flower.circle(50, 90)  # Draw half-circle for leaf
        flower.left(90)
        flower.circle(50, 90)
        flower.end_fill()

    # Hide the turtle and display the screen
    flower.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_flower_with_longer_petals()
