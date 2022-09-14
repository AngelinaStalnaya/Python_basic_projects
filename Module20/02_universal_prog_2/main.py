def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def crypto(my_object):
    return [sym for index, sym in enumerate(my_object) if is_prime(index)]


print(crypto('О Дивный Новый мир!'))
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
