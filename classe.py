class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius;
        self.color = color;

circle = Circle(5, "red")
circle2 = Circle(color = "blue", radius = 5)

print(circle2.radius)
print(circle2.color)