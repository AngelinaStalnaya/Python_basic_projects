my_number = int(input('Введите num: '))


def num_line(num):
    if num >= 0:
        num_line(num - 1)
        print(num)

num_line(my_number)