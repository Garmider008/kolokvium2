'''
Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
Гармідер Анастасія 122В
'''
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
b=a[10:]#видаляємо 10 цифер
if b==[]:#якщо елементів не буде то це буде пустий список
    print('Видаю повідомлення')
else:
    print('Таких елементів немає')