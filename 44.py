''''
Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
Гармідер Анастасія 122В
'''''
c=0
for a in range(1,10):
    b=int(input('Введіть числа'))
    if b==a and b%3==0:#умова кратності і номеру
        c+=1
print('Кількість елементів',c)