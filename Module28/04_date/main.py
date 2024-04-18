

class Date:
    """
    Класс, проверяющий валидность даты и конвертирующий строку даты в объект
    класса с данными о дате, месяце и годе.
    """

    @classmethod
    def is_date_valid(cls, string: str) -> bool:
        """
        Метод, проверяющий числа даты на корректность
        :param string: строка вида dd-mm-yyyy
        :return: значение типа bool (True в случае валидности даты,
        False - при вводе некорректной даты)
        """
        res = [int(value) for value in string.split('-')]
        if res[1] > 12 or res[1] < 1 or res[2] > 10000 or res[2] < 0 or \
           res[0] < 0 or (res[0] > 29 and res[1] == 2) or \
           (res[0] > 30 and res[1] in [4, 6, 9, 11]) or\
           (res[0] > 31 and res[1] in [1, 3, 5, 7, 8, 10, 12]):
            return False
        return True

    @classmethod
    def from_string(cls, string: str) -> str:
        """
        Метод конвертации строки в объект класса Date, состоящий из числовых
        значений дня, месяца и года.
        :param string: строка вида dd-mm-yyyy
        :return: строку, выводящую данные, содержащиеся в объекте
        """
        date_list = [int(value) for value in string.split('-')]
        return f'День: {date_list[0]}\tМесяц: {date_list[1]}\tГод: {date_list[2]}'


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
print(Date.is_date_valid('29-02-2018'))
print(Date.is_date_valid('30-02-2023'))
print(Date.is_date_valid('32-12-2815'))
print(Date.is_date_valid('00-00-2020'))
print(Date.is_date_valid('265-58-1262'))
