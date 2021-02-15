#
# Программа для распределения билетов на экзамене случайным образом
#


from random import randint as r

students = int(input('Введите количество студентов: '))
max_bilet = int(input('Введите количество билетов: '))

if students > max_bilet:
    print()
    print("Внимание! Невозможно распределить билеты без повторений.")
    print("Количество билетов не может быть меньше количества студентов в группе.")
    print("Будет произведена остановка программы.")
    exit()

bilets = []

for _ in range(max_bilet * 5):
    x = r(1, max_bilet)
    if x not in bilets:
        bilets.append(x)
        
print()
for i, item in enumerate(bilets[:students]):
    print(f'Студент №{i + 1}: билет №{item}')
