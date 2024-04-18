def move(disk, first, third):
    if disk > 0:
            second = 6 - first - third
            move(disk-1, first, second)
            print(f'Переложить диск {disk} со стержня  номер {first} на стержень номер {third}')
            move(disk-1, second, third)

disk=int(input('Введите количество дисков: '))

move(disk, 1, 3)