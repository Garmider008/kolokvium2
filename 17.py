'''
Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200.
Гармідер Анастасія 122В
'''
from random import randint
c=0
for i in range(20):#діапазон
    p=randint(100,200)#масив
    if p%2>0:#умова
        c=c+p#сума
print('Сума елементів масиву дійсних чисел, що мають непарні номер:', c)