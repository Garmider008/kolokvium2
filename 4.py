'''
Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
Гармідер Анастасія 122В
'''
a=['abragem','aibragem','hidragem','heragen','miragen']#масив
w=str(input('Введіть буукву'))
for i in range(5):
    f=a[0]#перша буква в першому слові
    if f[0]==w:# якщо перша буква така сама як і введена то виводимо це слово
        print(a[0])
    a=a[1:]