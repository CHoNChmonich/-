#1
import math
print("Введите значение для переменной а(в градусах):",end="")
a=int(input())
p=math.pi
b=180/p
print("Угол равен данному количеству радиан:",end="")
print(a/b)
#2
import math
p=math.pi
print("Введите значение для переменной а(в радианах):",end="")
a=int(input())
b=180/p
print("Угол равен данному количеству градусов:",end="")
print(a*b)
#3
print("Введите значение стоимости конфет:",end="")
a=int(input())
print("Введите значение массы конфет №1:",end="")
x=int(input())
print("Введите значение массы конфет №2:",end="")
y=int(input())
print("Один килограм конфет стоит:",end="")
ans1=a/x
print("Y киллограм конфет стоит:",end="")
ans2=ans1*y
#4
print("Введите значение кол-ва часов:",end="")
t=int(input())
print("Скорость автомобиля №1:",end="")
v1=int(input())
print("Скорость автомобиля №2:",end="")
v2=int(input())
print("Введите значение расстояния между автомобилями:",end=""0)
s1=int(input())
v1=max(v1,v2)
v2=min(v1,v2)
V=v1-v2
s2=V*t
ans=s1+s2
print("Итоговое расстояние между автомобилями:",end="")
print(ans)
#5
print("Введите значение для переменной а:",end="")
a=int(input())
print("Введите значение для переменной b:",end="")
b=int(input())
if(a==0)and(b==0):
    print("Решений бесконечное множество")
elif(a==0):
    print("Решений нет")
else:
    print(b/a)
#6
print("Введите значение коэф. А1:")
a1=int(input())
print("Введите значение коэф. B1:")
b1=int(input())
print("Введите значение коэф. C1:")
c1=int(input())
print("Введите значение коэф. А2:")
a2=int(input())
print("Введите значение коэф. B2:")
b2=int(input())
print("Введите значение коэф. C2:")
c2=int(input())
det=a1*b2-a2*b1
det1=c1*b2-b1*c2
det2=a1*c2-c1*a2
if(det==0)and(det1!=0 or det2!=0):
    print("Нет решений")
elif(det==0)and(det1==0)and(det2==0):
    print("Бесконечное кол-во решений")
else:
    x=det1//det
    y=det2//det
    print("x=",x,"y=",y)


