'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
Гармідер Анастасія 122В
'''
from random import randint
c=0
for i in range(10):
    h = randint(10, 20)
    if h>=-2 and h<=10:
        c=c+h
print('Середнє арифметичне значення',c/10)