
class Property:

    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def set_tax(self):
        self.tax = self.__worth / 100
        return self.tax


class Apartment(Property):

    def __init__(self, worth):
        super().__init__(worth)
        # self.tax = self.set_tax()

    def set_tax(self):
        self.tax = self.get_worth() / 1000
        print(f'Налог на квартиру составил: {self.tax}')
        return self.tax


class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def set_tax(self):
        self.tax = self.get_worth() / 200
        print(f'Налог на автомобиль составил: {self.tax}')
        return self.tax


class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)

    def set_tax(self):
        self.tax = self.get_worth() / 500
        print(f'Налог на дачу составил: {self.tax}')
        return self.tax


your_money = int(input('Введите количество денег на счету: '))
flat = Apartment(int(input('Введите стоимость квартиры: ')))
car = Car(int(input('Введите стоимость автомобиля: ')))
country_house = CountryHouse(int(input('Введите стоимость дачи: ')))
all_taxes = flat.set_tax() + car.set_tax() + country_house.set_tax()

if your_money - all_taxes > 0:
    print(f'Общая стоимость налогов на имущество составила {all_taxes}.У Вас достаточно денег на выплату налогов')
else:
    print(f'У Вас недостаточно денег для выплаты налогов. Найдите ещё {all_taxes - your_money}')
