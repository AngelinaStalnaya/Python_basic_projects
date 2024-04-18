
class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):

    def set_salary(self):
        self.salary = 1000
        return self.salary

    def __str__(self):
        print(f'Имя работника: {self.get_name()}\n'
              f'Фамилия работника: {self.get_surname()}\n'
              f'Возраст работника: {self.get_age()}\n'
              f'Заработная плата работника: {self.set_salary()}\n')


class Manager(Employee):

    def set_salary(self):
        self.salary = 13000
        return self.salary


class Agent(Employee):

    sales_amount = 5e10

    def set_salary(self):
        self.salary = 5000 + self.sales_amount * 0.05
        return self.salary


class Worker(Employee):

    working_hours = 180

    def set_salary(self):
        self.salary = 100 * self.working_hours
        return self.salary


my_office = []
my_office.extend([Manager(input('Введите имя: '),
                          input('Введите фамилию: '),
                          input('Введите возраст: ')) for _ in range(3)])
my_office.extend([Agent(input('Введите имя: '),
                        input('Введите фамилию: '),
                        input('Введите возраст: ')) for _ in range(3)])
my_office.extend([Worker(input('Введите имя: '),
                         input('Введите фамилию: '),
                         input('Введите возраст: ')) for _ in range(3)])
print(f'+{"+":-^21}+')
for person in my_office:
    person.__str__()