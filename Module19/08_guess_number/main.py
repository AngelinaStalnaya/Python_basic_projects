import random

number = int(input('Введите максимальное число: '))
artem = str(random.randint(1, number))
answer = ''
possible_answer = []
not_in_artem = []


boris = (input('Нужное число есть среди вот этих чисел: ')).split()

while boris != 'Помогите!'.split():
    if artem in boris:
        answer = 'Да'
        if len(possible_answer) < 1:
            possible_answer = boris
        if len(boris) < len(possible_answer):
            possible_answer = boris
    else:
        answer = 'Нет'
        not_in_artem.append(boris)
    print('Ответ Артёма: ', answer)
    print()
    boris = (input('Нужное число есть среди вот этих чисел: ')).split()

true_set = set(possible_answer)

print('Артём мог загадать следующие числа: ', ' '.join([num for num in true_set if num not in not_in_artem]))