'''''
Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
Гармідер Анастасія 122В
'''''
import numpy as np#импортируем библиотеку нампи
import random
s=0
c=0
b=np.zeros(10,dtype=int)#инициализируем масив нулями и присваиваем типу данных тип данных инт
for i in range(10):#проходимся по елементам масив
      b[i] = random.randint(-3,3)
for k in range(10):#снова проходимся
        s+=b[k]/10#Ищем среднюю температуру
for o in range(10):
    if b[o]>s: #если елементы больше среднего значения,счетчик +1
           c+=1
print('Средняя температура',s)
if c==2 or c==3 or c==4:
      print('Выше была',c,'раза')
else:
        print('Выше была',c,'раз')