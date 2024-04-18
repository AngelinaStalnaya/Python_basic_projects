len_of_protocol = int(input('Сколько записей вносится в протокол? '))
data_players = []
winners_names = []


print('Записи (результат и имя):')
for i in range(len_of_protocol):
    i_data = list(input(f'{i + 1}-я запись: ').split(' '))
    data_players.append(i_data)


print('Итоги соревнований: ')
for i in range(3):
    max_score = 0
    winner_name = ''
    for j in range(len(data_players)):
        if int(data_players[j][0]) > max_score and data_players[j][1] not in winners_names:
            max_score = int(data_players[j][0])
            winner_name = data_players[j][1]
            max_index = j
    winners_names.append(winner_name)
    print(f'{i + 1}-е место. {winner_name} ({max_score})')
    data_players.pop(max_index)

