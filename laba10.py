#1
def f(a,b):
    if(a>2)and(b<=3):
        return True
    return False
print("Введите значение для переменной а:",end="")
a=int(input())
print("Введите значение для переменной b:",end="")
b=int(input())
if(f(a,b)):
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
#2
def f(a,b,c):
    if(a<b)and(b<c):
        return True
    return False
print("Введите значение для переменной а:",end="")
a=int(input())
print("Введите значение для переменной b:",end="")
b=int(input())
print("Введите значение для переменной c:",end="")
c=int(input())
if(f(a,b,c)):
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
#3
print("Введите число:",end="")
x=int(input())
def f(x):
    c=0
    while(x>0):
        x=x//10
        c+=1
    if(c==2):
        return True
    return False
if(f(x)):
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
#4
print("Введите число:",end="")
x=input()
x1=int(x[0])
x2=int(x[1])
x3=int(x[2])
def f(a,b,c):
    if((a<b)and(b<c))or((a>b)and(b>c)):
        return True
    return False
if(f(x1,x2,x3)):
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
#5
print("Введите число:",end="")
x=input()
x1=int(x[0])
x2=int(x[1])
x3=int(x[2])
x4=int(x[3])
if(x1==x4)and(x2==x3):
    print("True")
else:
    print("False")
#6
print("Введите значение для стороны треугольника №1:",end="")
a=int(input())
print("Введите значение для стороны треугольника №2:",end="")
b=int(input())
print("Введите значение для стороны треугольника №3:",end="")
c=int(input())
if(a**2+b**2==c**2)or(a**2+c**2==b**2)or(b**2+c**2==a**2):
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
#7
print("Введите значение для стороны треугольника №1:",end="")
a=int(input())
print("Введите значение для стороны треугольника №2:",end="")
b=int(input())
print("Введите значение для стороны треугольника №3:",end="")
c=int(input())
def f(a,b,c):
    if(a+b>c)or(a+c>b)or(b+c>a):
        return True
    return False
if(f(a,b,c)):
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
