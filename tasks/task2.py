import turtle
import argparse

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)

def draw_snowflake(level):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    
    for _ in range(3):
        koch_snowflake(t, 300, level)
        t.right(120)
    
    t.hideturtle()
    screen.mainloop()

def main():
    print("Starts drawing")
    parser = argparse.ArgumentParser(description="Draw a Koch Snowflake fractal.")
    parser.add_argument("level", type=int, help="Recursion depth level")
    args = parser.parse_args()
    draw_snowflake(args.level)

if __name__ == "__main__":
    main()
