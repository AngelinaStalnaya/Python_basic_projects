import random


def f(x, y):
    x += random.randint(0, 5)
    y += random.randint(0, 10)
    return x / y


def f2(x, y):
    x -= random.randint(0, 5)
    y -= random.randint(0, 10)
    return y / x


res1 = None
res2 = None

with open('coordinates.txt', 'r') as file,\
     open('result.txt', 'w') as file_2:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            if not res1:
                raise Exception("Что-то пошло не так с первой функцией")
        # except Exception as exc:
        #     print("Что-то пошло не так с первой функцией")
        # try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            if not res2:
                raise Exception("Что-то пошло не так со второй функцией")
            # try:
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            file_2.write(' '.join(map(str, my_list)) + '\n')
            if not file_2:
                raise Exception("Что-то пошло не так c записью нового файла")
        except ZeroDivisionError:
            print('Деление на ноль запрещено.')
        except BaseException:
            print('Что-то пошло не так.')



file_to = open('result.txt', 'r')
for i_line in file_to:
    print(i_line.rstrip())
file_to.close()
