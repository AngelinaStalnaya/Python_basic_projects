def calculating_math_func(data):
    def factorial_num(data):
        if data == 1:
            return 1
        else:
            return data * factorial_num(data - 1)
    answer = factorial_num(data)
    def power_of_num(num, power):
        if power == 1:
            return num
        else:
            return num * power_of_num(num, power - 1)
    answer_2 = answer / power_of_num(data, 3)
    answer_3 = power_of_num(answer_2, 10)
    return answer_3


print(calculating_math_func(5))
