'''
Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
Гармідер Анастасія 122В
'''
import numpy as np#импортируем библиотеку нампи
c=1
b=np.zeros(10,dtype=int)#инициализируем масив нулями и присваеиваем типу данных тип данных инт
for i in range(10):#проходимся по елементам масива
      b[i] = input('Введите элементы: ')
for k in range(10):#снова проходимся
    l=b[k]#помещаем элементы в пустую переменную
    if l<=0:
         c*=l#если  значения меньше 0,перемножаем их
    if c==1:
         print('Нету отрицательных чисел')
    else:
         print('Сумма элементов нечетных индексов',c)