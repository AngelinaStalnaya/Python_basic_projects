# a = [{"x": 4}, "b", "z", "d"]
# b = (10, {20,}, [30], "z")
#
# k = [1, 2, 3, 4, 5]
# t = {1: "s", 2: "q", 3: 4}
# x = (1, 2, 3, 4, 5)

def my_zip(*args):
    min_len = min(len(element) for element in args)
    my_list = [tuple(arg[i] for arg in map(list, args)) for i in range(min_len)]
    return my_list

# print(my_zip(a, b))
# print(my_zip(k, t, x))