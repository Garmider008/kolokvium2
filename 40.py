'''''
Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
Гармідер Анастасія 122В
'''''
import numpy as np
c=0
b=np.zeros(5,dtype=int)
for i in range(5):#проходимся по елементам масива
      b[i] = int(input('Введите значение'))
for k in range(5):#снова проходимся
      if b[k]%2==0:#если элемент парный то сумируем их в наш счетчик,но если переберая значения масива встретится 0,выход из цикла
          if b[k]==0:
              break
          else:
              c+=b[k]
print(c)