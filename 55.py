'''
У будинку, що складається з 30 квартир, переселити мешканців так, щоб
мешканці першої квартири переїхали в тридцяту, з тридцятого - в першу, з другої - в 29
і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
Гармідер Анастасія 122В
'''
import numpy as np#импортируем библиотеку нампи
import random
b=np.zeros(30,dtype=int)#инициализируем масив нулями и присваеиваем типу данных тип данных инт
for i in range(30):#проходимся по елементам масива
      b[i] = random.randint(1,10)#генерируем значения
p=0
p=b[::-1]#переворачиваем наш масив с помощью среза
print(p)
c=0
for k in range(30):#Когда количество жильцов больше 5,счетчик +1
        if p[k]>5:
            c+=1
print(c)