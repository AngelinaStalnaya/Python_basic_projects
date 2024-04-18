import re

if __name__ == '__main__':

    pattern = r'\b[8-9]\d{9}'
    my_list = ['9999999999', '999999-999', '99999x9999', '8523698521', '721365', '7569852012']

    for tel in range(len(my_list)):
        print(f'{tel + 1}й номер: {"всё в порядке" if re.match(pattern, my_list[tel]) else "не подходит"}')
