import random


total_karma = 0
days = 0


class KillError(Exception):

    def __init__(self):
        super().__init__('"Вы кого-то убили."')


class DrunkError(Exception):

    def __init__(self):
        super().__init__('"Вы напились и натворили "дел""')


class CarCrashError(Exception):

    def __init__(self):
        super().__init__('"Вы попали в аварию"')


class GluttonyError(Exception):

    def __init__(self):
        super().__init__('"Вы объелись.Снова"')


class DepressionError(Exception):

    def __init__(self):
        super().__init__('"Вы сегодня были депрессивны"')


def one_day():
    today = random.randint(1, 7)
    try:
        if random.randint(1, 10) == 1:
            exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
            raise exception
    except Exception as exception:
        with open('karma.log', 'a', encoding='utf-8') as errors_file:
            errors_file.write(f'В {days} день Вы не получили очки кармы, поскольку произошла ошибка {exception}\n')
    return today


while total_karma < 500:
    days += 1
    result = one_day()
    if isinstance(result, int):
        total_karma += result


print(f'Вам понадобилось {days} дней чтобы набрать 500 очков кармы.\n')
print('Содержимое файла "karma.log":\n')
file_from = open('karma.log', 'r', encoding='utf-8')
for i_line in file_from:
    print(i_line.rstrip())
file_from.close()
