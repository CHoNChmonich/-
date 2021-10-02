#1
print("Введите значение переменной а:",end="")
a=int(input())
print("Введите значение переменной b:",end="")
b=int(input())
if(a>b):
    b=a
elif(b>a):
    a=b
else:
    a=0
    b=0
print("Значения переменных а и b:",end="")
print(a,b)
#2
print("Введите значение для числа №1:",end="")
a=int(input())
print("Введите значение для числа №2:",end="")
b=int(input())
print("Введите значение для числа №3:",end="")
c=int(input())
m=min(a,b,c)
ans=a+b+c-m
print("Сумма жвух максимальных чисел равна:".end="")
print(ans)
#3
import math
print("Введите значение координаты х для точки 1:",end="")
a1=int(input())
print("Введите значение координаты x для точки 2:",end="")
b1=int(input())
print("Введите значение координаты x для точки 3:",end="")
c1=int(input())
print("Введите значение координаты y для точки 1:",end="")
a2=int(input())
print("Введите значение координаты y для точки 2:",end="")
b2=int(input())
print("Введите значение координаты y для точки 3:",end="")
c2=int(input())
ac2=(a1-c1)**2+(a2-c2)**2
ab2=(a1-b1)**2+(a2-b2)**2
ac=math.sqrt(ac2)
ab=math.sqrt(ab2)
print("Ближайшая точка имеет координаты:",end="")
if(ac>ab):
    print(b1,b2)
    print("а ее расстояние равно:",end="")
    print(ab)
else:
    
    print(c1,c2)
    print("а ее расстояние равно:",end="")
    print(ac)
#4
print("Введите значение координаты х для точки:",end="")
x=int(input())
print("Введите значение координаты y для точки:",end="")
y=int(input())
print("Точка находится в четверти номер:",end="")
if(x*y>0):
    if(x>0)and(y>0):
        print("1")
    else:
        print("3")
else:
    if(x<0):
        print("2")
    else:
        print("4")
#5
print("Введите число")
x=int(input())
if(x>0):
    print("положительное",end=" ")
elif(x<0):
    print("отрицательное",end=" ")
else:
    print("нулевое число",end=" ")
if(x%2==0)and(x!=0):
    print("четное число")
if(x%2!=0):
    print("нечетное число")
#6
print("Введите число")
x=int(input())
def f(x):
    c=0
    while(x>0):
        x=x//10
        c+=1
    return c
if(x%2==0):
    print("четное",end=" ")
    if(f(x)==1):
        print("однозначное число",end=" ")
    if(f(x)==2):
        print("двузначное число",end=" ")
    if(f(x)==3):
        print("трехзначное число",end=" ")
else:
    print("нечетное",end=" ")
    if(f(x)==1):
        print("однозначное число",end=" ")
    if(f(x)==2):
        print("двузначное число",end=" ")
    if(f(x)==3):
        print("трехзначное число",end=" ")

