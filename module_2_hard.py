import random

n = random.randint(3, 20)
result = []
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result.append(i)
            result.append(j)

print('Выпавшее число:', n)
print('Решение:', *result, sep='')
