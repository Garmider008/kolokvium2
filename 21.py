'''
Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Гармідер Анастасія 122В
'''
from random import randint
c=1
e=0
q=int(input('Введіть число:'))
for i in range(10):#діапазон
    b=randint(50,100)#рандом
    if b<q:#умова
        e+=1#перевіряємо чи є такі числа щоб в кінці не вийшла 1
        c=c*b#сума
if e==0:
    print(0)
else:
    print('Добуток всіх елементів масиву дійсних чисел, менших заданого числа',c)