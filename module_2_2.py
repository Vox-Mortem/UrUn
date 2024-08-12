first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and second == third:
    q = 3
elif first == second or first == third or second == third:
    q = 2
else:
    q = 0
print('Количество одинаковых чисел: ', q)
