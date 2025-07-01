from random import randint

N = 10  # количество элементов в списке

a=[14, 28, 36, 95, 48, 14, 20, 15, 97, 82]
# Сама сортировка методом "пузырька"
for i in range(N-1):
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)  # вывод отсортированного списка