'''''
Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
Гармідер Анастасія 122В
'''''
import numpy as np#импортируем библиотеку нампи
s = 0
b=np.zeros(5,dtype=int)
for i in range(5):#проходимся по елементам масива
      b[i] = int(input('Введите ваши элементы '))
for k in range(5):#снова проходимся
       if b[k]>0:
           s+=b[k]
print(s)