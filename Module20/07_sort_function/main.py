def tpl_sort(user_tuple):
    new_list = []
    for number in (user_tuple):
        if isinstance(number, int) == True:
            new_list.append(number)
        else:
            new_list.append('stop')
            break
    if 'stop' in new_list:
        return user_tuple
    else:
        new_list.sort()
        return tuple(new_list)


# print(tpl_sort((6, 3, -1, 8, 4, 10, -5, 5.3)))
# print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))