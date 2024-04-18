class_1 = []
class_2 = []
both_classes = []

for height in range(160, 177, 2):
    class_1.append(height)
for height in range(162 , 181, 3):
    class_2.append(height)

both_classes.extend(class_1 + class_2)
both_classes.sort()
print('Отсортированный список учеников:', both_classes)
