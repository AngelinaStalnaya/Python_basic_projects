import random


class Student:

    def __init__(self, name, group=2210):
        self.name = name
        self.group_number = group
        self.progress = Student.current_progress(self)

    def current_progress(self):
        curr_progress = []
        # disciplines = ['Математика', 'Физика', 'Биология', 'Иностранный язык', 'Русский язык']
        for _ in range(5):
            mark = random.randint(5, 10)
            # mark = int(input(f'Введите оценки по предметам "{disciplines[i]}": '))
            curr_progress.append(mark)
        return curr_progress

    def student_info(self):
        print(f'\nФ.И.: {self.name}\n'
              f'Номер группы: {self.group_number}\n'
              f'Успеваемость: {self.progress}\n'
              f'Средний балл: {sum(self.progress)/5}\n')

    def rank_progress(self):
        self.rank = sum(self.progress)/5
        return self.rank


students_dict = dict()
for i in range(10):
    students_dict[f'student_{i + 1}'] = Student(input('Введите Ф.И. студента: '))

print(f"+{'+':-^57}+")
print('Рейтинг студентов по возрастанию среднего балла: ')

sorted_progress = sorted(students_dict[student].rank_progress() for student in students_dict)

sorted_students = dict()
for rank in sorted_progress:
    for i_student in students_dict:
        if rank == students_dict[i_student].rank_progress():
            if i_student not in sorted_students:
                sorted_students[i_student] = students_dict[i_student].student_info()