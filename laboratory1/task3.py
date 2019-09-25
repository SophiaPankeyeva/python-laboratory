print("Лабораторна робота №1 завдання3 \nПанкєєва Софія КМ-93 вар.№15")
while True:
    print('Введите значение x для решения уравнения ')
    r=True
    while r:
        try: x = float(input('x='))
        except:
            print('Вы пытаетесь ввести букву? Не тут то было.')
            continue
        else:r=False
    if x>3.6:
        a=45*x**2+5
        print('Значение x больше 3.6, результат ')
        print(a)
    else:
        a=(5*x)/(10*x**2+1)
        print('Значение меньше или равно 3.6, результат')
        print(a)