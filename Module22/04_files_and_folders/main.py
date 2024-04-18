import os




ending = (input('Введите путь: '))
data = {'size_dir': 0,
        'count_dirs': 0,
        'count_files': 0}

def find_folder(path, file_name):
    if os.path.isdir(path):
        for i_elem in os.listdir(path):
            new_path = os.path.join(path, i_elem)
            if new_path.endswith(file_name):
                return new_path
            else:
                result = find_folder(new_path, file_name)
                if result:
                    return result

def get_data(path, data):
    for elem in os.listdir(path):
        i_elem = os.path.join(path, elem)
        if os.path.isdir(i_elem):
            data['count_dirs'] += 1
            get_data(i_elem, data)
        if os.path.isfile(i_elem):
            data['count_files'] += 1
            data['size_dir'] += os.path.getsize(i_elem)
    return data


abs_path = find_folder(r'C:\Users\Public', ending)
print('Абсолютный путь: ', abs_path)
all_data = get_data(abs_path, data)
print('Размер каталога (в Кб): ', all_data['size_dir'] / 1024)
print('Количество подкаталогов: ', all_data['count_dirs'])
print('Количество файлов: ', all_data['count_files'])
