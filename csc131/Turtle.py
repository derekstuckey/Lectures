import turtle


def draw_square(t,x,y, length):
    """Draws a square with the given turtle t, an upper-left corner point(x,y), and a sides length"""
    t.up()
    t.goto(x,y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)


def radial_hexagon(t, n, length):
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)


def radial_pattern(t: Turtle, n: int, length: int, shape) -> None:
    """
    Draws a radial pattern of n shapes with the given length
    :param t: a Turtle instance
    :param n: number of shapes
    :param length: length of the shape side
    :param shape: a function for drawing some shape
    :return: None
    """
    for count in range(n):
        shape(t, length)
        t.left(360 / n)


def main():
    wn = turtle.Screen()
    derek = turtle.Turtle()
    radialHexagon(0,0,250)


if __name__ == '__main__':
    main()