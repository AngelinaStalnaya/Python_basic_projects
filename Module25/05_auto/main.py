import math


class Auto:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, direction):
        self.x += direction * math.cos(self.angle)
        self.y += direction * math.sin(self.angle)


class Bus(Auto):

    km_cost = 0.3
    max_passengers = 50

    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.passengers = 0
        self.money = 0

    def take_a_bus(self, people):
        if self.passengers < self.max_passengers:
            self.passengers += people
            if self.passengers > self.max_passengers:
                over_crowded = self.passengers - self.max_passengers
                print(f'Автобус полон. В автобус не поместилось {over_crowded} человек')
        else:
            print('Автобус полон.')

    def leave_bus(self, people):
        if self.passengers == 0:
            print('Автобус пуст.')
        elif self.passengers < people:
            print(f'Автобус покинуло {self.passengers} человек')
        else:
            self.passengers -= people
            print(f'Автобус покинуло {people} человек')

    def move(self, distance):
        self.money += self.passengers * distance * self.km_cost
        super().move(distance)
        self.__str__()

    def __str__(self):
        print(f'Количество пассажиров: {self.passengers}\n'
              f'Количество денег: {round(self.money, 2)}\n'
              f'Координаты нахождения: {round(self.x)}:{round(self.y)}\n')


bus = Bus(0, 0, 45)
bus.take_a_bus(7)
bus.move(15)
bus.leave_bus(3)
bus.move(3)
bus.take_a_bus(23)
bus.move(25)
bus.leave_bus(15)
bus.move(10)
bus.leave_bus(10)
bus.move(12)
bus.leave_bus(12)
bus.move(45)
