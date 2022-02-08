people = int(input('Кол-во человек: '))
step = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', step, 'человек')
circle = []
minus = 0
start = 1
delete = 0
for i in range(1, people + 1):
    circle.append(i)

for person in range(people - 1):
    print()
    circle.sort()
    print('Текущий круг людей: ', circle)
    print('Начало счёта с номера ', start)
    num = circle.index(start)
    circle = circle[num:] + circle[:num]
    if len(circle) == 2:
        break
    else:
        if step > len(circle):
            minus = step - len(circle)
            if minus > len(circle):
                minus -= len(circle)
        else:
            minus = step
        delete = circle[minus - 1]
        print('Выбывает человек под номером: ', delete)
        if delete == max(circle):
            start = min(circle)
        else:
            start = delete + 1
            while start not in circle:
                start += 1
        circle.pop(minus-1)
if step % 2 == 0:
    print('Выбывает человек под номером: ', str(circle[1]))
    print()
    print('Остался человек под номером ', str(circle[0]))
else:
    print('Выбывает человек под номером: ', str(circle[0]))
    print()
    print('Остался человек под номером ', str(circle[1]))

