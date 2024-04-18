import math


class Circle:

    def __init__(self, coordinate_x=0, coordinate_y=0, radius=1):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.radius = radius

    def find_area(self):
        self.area = round(math.pi * self.radius ** 2, 3)
        return self.area

    def find_perimeter(self):
        self.perimeter = round(2 * math.pi * self.radius, 3)
        return self.perimeter

    def enlarge(self, multiplier):
        return self.radius * multiplier

    def intersection(self, circle):
        distance_c1_to_c2 = self.radius + circle.radius
        x_diff = abs(self.coordinate_x - circle.coordinate_x)
        y_diff = abs(self.coordinate_y - circle.coordinate_y)
        if self.coordinate_x == circle.coordinate_x: # если одинаковые х
            if distance_c1_to_c2 > x_diff:
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        elif self.coordinate_y == circle.coordinate_y: # если одинаковые у
            if distance_c1_to_c2 > y_diff:
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        else: # если координаты точек разные
            if distance_c1_to_c2 ** 2 > x_diff ** 2 + y_diff ** 2:
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')


circle1 = Circle(1, 3, 2)
circle2 = Circle(2, 4)

circle1.intersection(circle2)



