'''
Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Гармідер Анастасія 122В
'''
from random import randint
c=0
o=int(input('Введіть число:'))
for i in range(20):#діапазон
    b=randint(50,100)#рандом
    if b>o:#умова
        c=c+b#сума
print('Сума всіх елементів масиву дійсних чисел, більших за задане число:',c)