from random import randint
import time

N = 10  # количество элементов в списке

a = [14, 28, 36, 95, 48, 14, 20, 15, 97, 82,14, 28, 36, 95, 48, 14, 20, 15, 97, 82,14, 28, 36, 95, 48, 14, 20, 15, 97, 82,14, 28, 36, 95, 48, 14, 20, 15, 97, 82,14, 28, 36, 95, 48, 14, 20, 15, 97, 82,14, 28, 36, 95, 48, 14, 20, 15, 97, 82]

# Start the timer
start_time = time.time()

# Сама сортировка методом "пузырька"
for i in range(N-1):
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

# Stop the timer
end_time = time.time()

print(a)  # вывод отсортированного списка
print(f"Execution time: {end_time - start_time} seconds")