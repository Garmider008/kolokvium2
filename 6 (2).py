'''''
Створіть масив А [1..8] за допомогою генератора випадкових чисел зелементами від -10 до 10 і виведіть його на екран. 
Підрахуйте кількість від’ємних елементів масиву.
Гармідер Анастасія 122В
'''''
import numpy as np#импортируем библиотеку нампи
import random
count=0
b=np.zeros(8,dtype=int)#инициализируем масив нулями и присваиваем типу данных тип данных инт
for i in range(8):#проходимся по елементам масива
      b[i] = random.randint(-10,10)
for k in range(8):#снова проходимся
     if b[k]<0: #если элементы меньше 0,счетчик увеличивается на 1
           count+=1
print('Количество отрицательных элементов',count)
