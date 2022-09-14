def slicer(input_tuple, num):
    my_tuple = ()
    indexes = []
    step = 0
    for i_index in input_tuple:
        if i_index == num:
            indexes.append(step)
        step += 1

    if len(indexes) >= 2:
        my_tuple = input_tuple[indexes[0]:indexes[1] + 1]
    elif len(indexes) == 1:
        my_tuple = input_tuple[indexes[0]:]
    else:
        my_tuple = ()
    return my_tuple



# element = int(input('Введите элемент: '))
# print(slicer((5, 7, 9, 11, 13, 7, 19, 7, 15), element))
# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 11))
# print(slicer((5, 7, 9, 11, 13, 15), element))
# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
