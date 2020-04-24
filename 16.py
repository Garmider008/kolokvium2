'''
Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
Гармідер Анастасія 122В
'''
import numpy as np
import random
A=np.zeros(15,dtype=int)
r=1
for i in range(len(A)):
    A[i]=random.randint(10,50)
    if A[i]%7==0:
        r*=A[i]
print(A)
print(f'Результат: {r}')
