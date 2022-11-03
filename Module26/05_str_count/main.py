import os
from collections.abc import Iterable


def find_py_files(path: dir) -> Iterable[int]:
    """
    Генератор подсчета строк кода в файлах расширения ".ру" в указанной директории
    :param path: передаваемая директория для перебора содержащихся файлов
    :return: None
    """
    for i_elem in os.listdir(path):
        new_path = os.path.abspath(os.path.join(path, i_elem))
        if os.path.isfile(new_path) and new_path.endswith('.py'):
            with open(new_path, 'r', encoding='utf-8') as file_from:
                all_lines = 0
                for i_line in file_from:
                    i_line.rstrip()
                    if i_line != '\n' and not i_line.startswith('#') and not i_line.startswith('"'):
                        all_lines += 1
                yield all_lines
        else:
            find_py_files(new_path)


my_path = r'C:\Users\Public\Python_Basic\Module24\07_cohabitation'
my_files = find_py_files(my_path)
all_lines_count = 0
for i in my_files:
    all_lines_count += i
print('Общее количество строк кода в файлах расширения ".py" в указанной директории: ', all_lines_count)
