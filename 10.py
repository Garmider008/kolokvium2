'''''
Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
Гармідер Анастасія 122В
'''''
r = []
c = 0
for i in range(30):
    r.append(int(input("Введіть декаду листопада:")))
for i in range(30):
    if r[i] < 10:
        c += 1
print("Число разів скільки температура була нижче -10: ",c)
