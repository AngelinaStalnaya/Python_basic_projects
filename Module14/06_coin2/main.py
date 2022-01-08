# Задача 6. Монетка 2

print('Введите координаты монетки: ')
x_point = float(input('X: '))
y_point = float(input('\n Y: '))
radius = float(input('Введите радиус: '))

if x_point <= radius and y_point <= radius:
    print('Монетка где-то рядом')
else:
    print ('Монетки в области нет')