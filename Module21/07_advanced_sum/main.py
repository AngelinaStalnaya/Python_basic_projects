def summ(*args):
    sum = 0
    for argument in args:
        if isinstance(argument, int):
            sum += argument
        else:
            for i_elem in argument:
                sum += summ(i_elem)
    return sum


print('Ответ: ', summ([[1, 2, [3]], [1], 3]))
print('Ответ: ', summ(1, 2, 3, 4, 5))
