#1
print("Введите значение для переменной А")
A=5
print("Введите значение для переменной В")
B=10
t=A
A=B
B=t
print("Значениея переменных А и В")
print(A,B)
#2
print("Введите значение для переменной А:",end="")
a=int(input())
print("Введите значение для переменной B:",end="")
b=int(input())
print("Введите значение для переменной C:",end="")
c=int(input())
t=a
y=b
u=c
b=t
c=y
a=u
print("Значения переменных А,B и С:",end="")
print(a,b,c)
#3
print("Введите значение для переменной А:",end="")
a=int(input())
print("Введите значение для переменной B:",end="")
b=int(input())
print("Введите значение для переменной C:",end="")
c=int(input())
a1=a
b1=b
c1=c
c=a1
b=c1
a=b1
print("Значения переменных А,B и С:",end="")
print(a,b,c)
#4
print("Введите значение для переменной х:",end="")
x=int(input())
y=3*(x**6)-6*(x**2)-7
print("Значение у равно",end="")
print(y)
#5
print("Введите значение для перменной х:",end="")
x=int(input())
y=4*((x-3)**6)-7*((x-3)**3)+2
print("Значение у равно",end="")
print(y)
#6
print("Введите значение для переменной а:",end="")
a=int(input())
b=a
a1=a*b
b=a1
a2=a1*b
b=a2
a3=a2*b
print("Значение а**8 равно",end="")
print(a3)
#7
print("Введите значение для переменной а:",end="")
a=int(input())
b=a
c=a
c=a*b
a=c*b
b=a*c
c=b
a=b
a=c*b
c=a
a=c*b
print("Значение а**15 равно",end="")
print(a)


