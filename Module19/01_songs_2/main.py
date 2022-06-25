violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}


total_length = 0
songs = ['первой', 'второй', 'третьей', 'четвёртой', 'пятой', 'шестой', 'седьмой', 'восьмой', 'девятой']
songs_num = int(input('Сколько песен выбрать? '))
for i in range(songs_num):
    print('Название', songs[i], end='')
    song_name = input(' песни: ')
    if song_name in violator_songs.keys():
        total_length += violator_songs[song_name]

print('Общее время звучания песен: ', total_length, 'минуты')
