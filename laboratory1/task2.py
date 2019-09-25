print("Лабораторна робота №1 завдання2 \nПанкєєва Софія КМ-93 вар.№15")
while True :
    print( 'введіть потрібний вам вік age= ')
    r = True
    while r:
        try: age = int(input())
        except:
            print('введіть, будь ласка, числові значення ')
            continue
        else: r = False
    if ( age>=0 ) and (age<6 ):
        print('дошкільник');
    elif ( 6<=age) and (age<23) :
        print('учень');
    elif (23<=age) and (age<60) :
        print ('працівник')
    elif(age>=60) and (age<=100):
        print ('пенсіонер');
    elif (age<0) :
        print ('ви ще не народились, введіть інше значення');
    elif (age >100 ) :
        print('думаю, ви вже померли. введіть інше значення ') ;