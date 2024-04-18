info = '80\nIvanov Serg 80\nSergeev Petr 92\nPetrov Vasiliy 98\nVasiliev Maxim 78'

file = open('first_tour.txt', 'w', encoding='utf-8')
file.write(info)
file.close()

participants = []
new_list = []


first_tour = open('first_tour.txt', 'r', encoding='utf-8')
print('Содержимое файла first_tour.txt:')
for i_line in first_tour:
    print(i_line.rstrip())
    participants.append(list(i_line.rstrip().split()))
first_tour.close()


num_k = int(participants[0][0])
nums = []
for i in participants:
    for elem in i:
        if elem.isdigit() and int(elem) > num_k:
            new_list.append(i)
            nums.append(int(elem))

nums.sort(reverse=True)

sec_part = []
for num in nums:
    for list in new_list:
        if str(num) in list:
            sec_part.append(list)

second_tour_participants = f'{len(new_list)}\n'

for i in range(len(sec_part)):
    name = sec_part[i][1][0]
    surname = sec_part[i][0]
    score = sec_part[i][2]
    new_info = f'{i+1}) {name}. {surname} {score}\n'
    second_tour_participants += new_info


second_file = open('second_tour.txt', 'w', encoding='utf-8')
second_file.write(second_tour_participants)
second_file.close()

second_tour = open('second_tour.txt', 'r', encoding='utf-8')
print('\nСодержимое файла second_tour.txt: ')
for i_line in second_tour:
    print(i_line.rstrip())
second_tour.close()