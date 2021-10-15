#1
def f(a,b):
    b=a**3
    return b

for i in range(5):
    print("Введите число А, а затем число B:",end="")
    print(f(int(input()),int(input())))

#2
print("Введите значение числа A:",end="")
a=int(input())
print("Введите значение числа B:",end="")
b=int(input())
def f(x):
    if(x<0):
        return -1
    if(x==0):
        return 0
    if(x>0):
        return 1
print("Вывод функции Sign:",end="")
print(f(a)+f(b))
#3
import math
print("Введите значение радиуса первой окружности:",end="")
x=int(input())
print("Введите значение радиуса второй окружности:",end="")
y=int(input())
def f(x,y):
    a=math.pi*x*x
    b=math.pi*y*y
    a,b=max(a,b),min(a,b)
    return a-b
print("Площадь колечка равна:",end="")
print(f(x,y))
#4
print("Введите значения координат x1 и y1(через пробел):",end="")
x1,y1=[int(s) for s in input().split()]
print("Введите значения координат x2 и y2(через пробел):",end="")
x2,y2=[int(s) for s in input().split()]
print("Введите значения координат x3 и y3(через пробел):",end="")
x3,y3=[int(s) for s in input().split()]
def f(x,y):
    if(x*y>0):
        if(x>0):
            return 1
        else:
            return 3
    else:
        if(x>0):
            return 4
        else:
            return 2
print("Эти точки находятся в следующих четвертях:")
print(f(x1,y1))
print(f(x2,y2))
print(f(x3,y3))
#5
print("Введите значение N:",end="")
n=int(input())
def f(n):
    k=n
    if(n%2!=0):
        for i in range(1,n):
            if(i%2!=0):
                k*=i
        return k
    else:
        for i in range(1,n):
            if(i%2==0):
                k*=i
        return k
print("Значение функции от N":,end="")
print(f(n))
                
