x = float(input())
y = float(input())
h = float(input())

#Walls
side_wall = x * y
window = 1.5 * 1.5

two_sideds = (2*side_wall) - (2*window)
back_wall = x * x
Door = 1.2 * 2
total_front_back = (2*back_wall) - Door
total=two_sideds + total_front_back

green_paint = total / 3.4
print("%.2f" % green_paint)

#Roof
roof_sides = 2 * (x*y)
roof_triangles = 2 * (x*h/2)
roof_total = roof_sides + roof_triangles
red_paint = roof_total / 4.3
print("%.2f" % red_paint)