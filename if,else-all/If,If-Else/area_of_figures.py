from math import pi

figure = input()

if (figure=="square"):
    square_value = float(input())
    square_face = float(square_value * square_value)
    print(f'{square_face:.3f}')
elif (figure == "rectangle"):
    rectangle_value_a = float(input())
    rectangle_value_b = float(input())
    rectangle_face = rectangle_value_a * rectangle_value_b
    print(f'{rectangle_face:.3f}')
elif (figure == "circle"):
    circle_value_a = float(input())
    circle_face = pi * (circle_value_a ** 2)
    print(f'{circle_face:.3f}')
elif (figure == "triangle" ):
    triangle_lenght = float(input())
    triangle_height = float(input())
    triangle_face = 0.5 * triangle_lenght * triangle_height
    print(f'{triangle_face:.3f}')