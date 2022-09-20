# summa = 0
#
# def advanced_sum(*args):
#     for argument in args:
#         if isinstance(argument, int):
#             global summa
#             summa += argument
#         else:
#             for i_arg in argument:
#                 advanced_sum(i_arg)
#     return summa
#
#
# print('Ответ: ', advanced_sum([[1, 2, [3]], [1], 3]))
# print('Ответ: ', advanced_sum(1, 2, 3, 4, 5))


# *****************all right******
summa = 0
def summ(*args):
    global summa
    summa = 0
    def advanced_sum(*args):
        def unpack_list(argument, list=[]):
            if isinstance(argument, int):
                list.append(argument)
                global summa
                summa += argument
            else:
                for i_elem in argument:
                    unpack_list(i_elem, list)
            return summa

        for argument in args:
            if isinstance(argument, int):
                global summa
                summa += argument
            else:
                return summa + unpack_list(argument)
        return summa
    return advanced_sum(*args)
# #
# print('Ответ: ', summ([[1, 2, [3]], [1], 3]))
# print('Ответ: ', summ(1, 2, 3, 4, 5))
