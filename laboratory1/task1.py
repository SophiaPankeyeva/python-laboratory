import math
print("Лабораторна робота №1 завдання2 \nПанкєєва Софія КМ-93 вар.№15")
print ('введіть діаметр основи циліндра ,а після нажміть enter : ')
diametr = float(input()) ;
print ('введіть висоту циліндра ,а після нажміть enter : ')
height = float(input()) ;
print ('введіть площу,яку можну забарвити однією банкою фарби ,а після нажміть enter : ')
area = float(input()) ;
N=math.ceil((math.pi*diametr*height+math.pi*diametr**2/2)/area)
print( "кількість банок =" + str (N))