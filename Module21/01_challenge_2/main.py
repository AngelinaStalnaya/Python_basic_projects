my_number = int(input('Введите num: '))
result = 0

def num_line(num, result):
    if result == num:
        return num
    else:
        result += 1
        print(result)
        return num_line(num, result)

num_line(my_number, result)