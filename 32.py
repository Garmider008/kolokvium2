'''
Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
Гармідер Анастасія 122В
'''
from random import randint
t=False#змінна яка при дотриманні певного умови стає True
for i in range(10):#діапазон
    r = randint(10, 20)  # масив
    if r<0 and r%2==0:#умова
            t=True
            break
print('Змінна набула значення:', t)