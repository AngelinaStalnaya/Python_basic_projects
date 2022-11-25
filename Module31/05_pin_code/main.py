import itertools

if __name__ == '__main__':

    numbers = range(10)
    combinations_list = [num_combination for num_combination in itertools.product(numbers, repeat=4)]
    for combination in combinations_list:
        print(combination)
