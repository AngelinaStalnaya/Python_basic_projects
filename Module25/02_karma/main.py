import random


total_karma = 0
days = 0

def one_day():
    errors = ('KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError')
    take_error = random.randint(1, 10)
    if take_error == 1:
        return errors[random.randint(0, 4)]
    else:
        return random.randint(1, 7)


while total_karma < 500:
    try:
        days += 1
        result = one_day()
        if isinstance(result, int):
            total_karma += result
        else:
            raise Exception
    except Exception as error:
        with open('karma.log', 'a', encoding='utf-8') as errors_file:
            errors_file.write(f'В {days} день Вы не получили очки кармы, поскольку произошла ошибка {error}\n')


print(f'Вам понадобилось {days} дней чтобы набрать 500 очков кармы.\n')
print('Содержимое файла "karma.log":\n')
file_from = open('karma.log', 'r', encoding='utf-8')
for i_line in file_from:
    print(i_line.rstrip())
file_from.close()
