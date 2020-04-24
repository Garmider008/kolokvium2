'''
Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
Гармідер Анастасія 122В
'''
import numpy as np
import random
A = np.zeros(20, dtype=int)
n = len(A)
u = int(input('Введите ваши числа:'))
t = False
c = 0
for i in range(n):
    A[i] = random.randint(-10, 10)
for i in range(n):
    if A[i] == max(A):
        c += 1
    if c == 1 and max(A) < u:
        t = True

print(t)
