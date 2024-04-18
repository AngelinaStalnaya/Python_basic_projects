import time

client = input('Введите имя пользователя: ')



while True:
    try:
        choice = input('1. Посмотреть текущий текст чата. \n2. Отправить сообщение. \nВыберите действие: ')
        if choice == '1':
            with open("client's_chat.txt", 'r', encoding='utf-8') as history_file:
                for i_line in history_file:
                    print(i_line.rstrip())
        elif choice == '2':
            with open("client's_chat.txt", 'a', encoding='utf-8') as history_file:
                cur_time = time.strftime("%H:%M:%S", time.localtime())
                message = input('Введите сообщение: ')
                history_file.write(f'В {cur_time} [{client} написал]: {message}\n')
        else:
            raise ValueError
    except ValueError:
        print('Ошибка выбора, попробуйте еще раз.')


# except EOFError:
# print('Текущий чат пуст, попробуйте позже.')