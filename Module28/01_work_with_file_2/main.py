import os
import datetime


class File:

    def __init__(self, path: dir) -> None:
        self.file = path
        self.mode = 'w'

    def __enter__(self):
        print('Открываем файл для записи.')
        self.file = open(self.file, self.mode, encoding=' utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True


path = os.path.abspath(os.path.join(os.curdir, 'task1_file2.txt'))


with File(path) as file:
    file.write(f'{datetime.datetime.now()} Всем привет!')

print()
print('Содержание файла: ')
file_from = open(path, 'r', encoding='utf-8')
for i_line in file_from:
    print(i_line)
file_from.close()
