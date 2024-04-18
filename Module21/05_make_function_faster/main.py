def factorial_num(num, my_dict=dict()):
    if num in my_dict:
        return my_dict[num]
    if num == 1:
        return 1
    fact = num * factorial_num(num-1, my_dict)
    my_dict[num] = fact
    return fact

def power(a, n):
    if n == 1:
        return a
    return a * power(a, n - 1)


def calculating_math_func(data, my_dict):
    if data > 1:
        result = factorial_num(data, my_dict)
    else:
        result = 1
    result /= power(data, 3)
    result = power(result, 10)
    return result

fact_dict = dict()


print(calculating_math_func(7, fact_dict))
