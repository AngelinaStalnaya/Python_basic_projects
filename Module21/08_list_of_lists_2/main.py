nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

new_list = []

def list_maker(*args):
    for i_element in args:
        if isinstance(i_element, int):
            new_list.append(i_element)
        else:
            for number in i_element:
                list_maker(number)
    return new_list




print(list_maker(nice_list))