'''''
Створіть цілочисельний масив А [1..15] за допомогою генератора випадкових чисел з елементами від -15 до 30 і виведіть його на екран. 
Визначте найбільший елемент масиву і його індекс.
Гармідер Анастасія 122В
'''''
import numpy as np
import random
p = 0
h = 0
a = np.zeros(12, dtype=int)
for i in range(12):
    a[i] = random.randint(1, 15)
print('Рандомні числа масиву', a)
for i in range(len(a)):
    if a[i] > h:
        h = a[i]
        p = i
print("Максимум:", h)
print("Його індекс", p+1)