import os
from collections.abc import Iterable


def gen_files_path(to_find_catalog: dir, cur_dir=os.path.abspath('C:/') or dir) -> Iterable[dir]:
    """
    Генератор поиска заданного каталога
    :param to_find_catalog: передается искомый каталог
    :param cur_dir: по умолчанию - корневой диск, иначе - заданная директория
    :return: None
    """
    for address, dirs, files in os.walk(cur_dir):
        for name in files:
            catalog = os.path.abspath(os.path.join(address, name))
            yield catalog
            if catalog.startswith(to_find_catalog) or catalog.endswith(to_find_catalog):
                print('Каталог найден.')
                return


my_directory = os.path.abspath('C:/Users/Public')
my_file = os.path.join('06_cohabitation_2', 'crazy_life.py')
my_file_2 = os.path.abspath('C:/Users/Public/Python_Basic/Module25')
my_file_3 = os.path.join('03_files_path', 'main.py')

function = gen_files_path(to_find_catalog=my_file, cur_dir=my_directory)
for i in function:
    print(i)
print()

# fuction_2 = gen_files_path(to_find_catalog=my_file_2, cur_dir=my_directory)
# for i in fuction_2:
#     print(i)
# print()
# ok!!

# functin_3 = gen_files_path(to_find_catalog=my_file_3, cur_dir=my_directory)
# for i in functin_3:
#     print(i)
# ok!!
