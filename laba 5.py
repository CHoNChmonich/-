#1
import math

def f(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist
print("Введите значение координаты х для точки 1:",end="")
x1=int(input())
print("Введите значение координаты y для точки 1:",end="")
y1=int(input())
print("Введите значение координаты х для точки 1:",end="")
x2=int(input())
print("Введите значение координаты y для точки 1:",end="")
y2=int(input())


print(f(x1,y1,x2,y2))

#2
print("Введите значение точки А:",end="")
a=int(input())
print("Введите значение точки B:",end="")
b=int(input())
print("Введите значение точки C:",end="")
c=int(input())
AC=a+c
BC=b+c
print("значение отрезка АС,значение отрезка ВС,значение суммы отрезков АС и АВ")
print(AC,BC,AC+BC)
#3
print("Введите значение точки А:",end="")
a=int(input())
print("Введите значение точки B:",end="")
b=int(input())
print("Введите значение точки C:",end="")
c=int(input())
k=0
AC=a+c
BC=b+c
if((c>=a)and(c<=b))or((c>=b)and(c<=a)):
    k=AC*BC
if(k==0):
    print("c не лежит между точками А и В")
print("произведение отрезков АС и ВС равно:",end="")
print(k)
#4
print("Введите значение координаты х для точки 1:",end="")
x1=int(input())
print("Введите значение координаты y для точки 1:",end="")
y1=int(input())
print("Введите значение координаты х для точки 2:",end="")
x2=int(input())
print("Введите значение координаты y для точки 2:",end="")
y2=int(input())

a=max(x1,x2)-min(x1,x2)
b=max(y1,y2)-min(y1,y2)
P=(a+b)*2
S=a*b
print("Периметр,площадь равны:",end="")
print(P,S)

#5
import math
def f(x1,y1,x2,y2):
    a=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return a
print("Введите значение координаты х для точки 1:",end="")
x1=int(input())
print("Введите значение координаты y для точки 1:",end="")
y1=int(input())
print("Введите значение координаты х для точки 2:",end="")
x2=int(input())
print("Введите значение координаты y для точки 2:",end="")
y2=int(input())
print("Введите значение координаты х для точки 3:",end="")
x3=int(input())
print("Введите значение координаты y для точки 3:",end="")
y3=int(input())
a=f(x1,y1,x2,y2)
b=f(x1,y1,x3,y3)
c=f(x2,y2,x3,y3)
p=(a+b+c)/2

S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Площадь, периметр равны:",end="")
print(S,p*2)

