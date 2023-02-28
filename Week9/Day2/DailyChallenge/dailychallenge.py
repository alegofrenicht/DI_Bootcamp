# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
#
#   - Compute the circle’s area
#   - Print the circle and get something nice
#   - Be able to add two circles together
#   - Be able to compare two circles to see which is bigger
#   - Be able to compare two circles and see if there are equal
#   - Be able to put them in a list and sort them


from math import pi


class Circle:

    def __init__(self, type_of_parameter, value):
        self.type = type_of_parameter
        self.value = value
        if self.type == 'radius':
            self.radius = self.value
            self.diameter = self.value * 2
        elif self.type == 'diameter':
            self.diameter = self.value
            self.radius = self.value / 2

    def circle_area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f"{self.print_circle()}"

    def print_circle(self):
        if self.type == 'radius':
            self.radius = self.value
            self.diameter = self.value * 2
        elif self.type == 'diameter':
            self.diameter = self.value
            self.radius = self.value / 2
        radius = self.diameter / 2 - .5
        r = (radius + .25) ** 2 + 1

        result = ''

        for i in range(self.diameter):
            y = (i - radius) ** 2
            for j in range(self.diameter):
                x = (j - radius) ** 2
                if x + y <= r:
                    result = result + '*  '
                else:
                    result = result + '   '
            result = result + '\n'
        return result

    def __gt__(self, other):
        return len(self.print_circle()) > len(other.print_circle())

    def __lt__(self, other):
        return len(self.print_circle()) < len(other.print_circle())

    def __ge__(self, other):
        return len(self.print_circle()) >= len(other.print_circle())

    def __le__(self, other):
        return len(self.print_circle()) <= len(other.print_circle())



circle_one = Circle('radius', 10)
circle_two = Circle('radius', 3)
circle_three = Circle('diameter', 3)
circle_four = Circle('radius', 6)
circle_five = Circle('diameter', 7)

circles = [circle_one, circle_two, circle_three, circle_four, circle_five]
circles.sort()

for circle in circles:
    print(circle)



