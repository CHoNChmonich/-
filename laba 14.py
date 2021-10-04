#1
print("Введите значение переменной А:",end="")
a=int(input())
print("Введите значение переменной В:",end="")
b=int(input())
for i in range(a,b+1):
    for j in range(i):
        print(i)
#2
print("Введите числовое значение для отрезка А:",end="")
a=int(input())
print("Введите числовое значение для отрезка B:",end="")
b=int(input())
while(a-b>0):
    a=a-b
print("Незанятая часть отрезка а по своей длине равна:",end="")
print(a)
#3
print("Введите значение для переменной n:",end="")
n=int(input())
for i in range(1,n):
    k=i
    s=k
    for j in range(1,i):
        s+=j
    if(s>=n):
        print("Наименьшее возможное подходящее число равно:",end="")
        print(k)
        break
#4
s=1000
k=0
print("Введите значение процентной ставки:",end="")
p=int(input())
while(s<=1100):
    k+=1
    s=s*(1+(p/100))
print("Необходимое количество месяцев равно:",end="") 
print(k)   
#5
print("Введите значение для числа А:",end="")
a=int(input())
print("Введите значение для числа B:",end="")
b=int(input())
while(a!=b):
    a,b=max(a,b),min(a,b)
    a=a-b
print("НОД этих чисел равен:",end="")
print(a)
#6
print("Введите число Фибоначчи")
n=int(input())
a=[0]*10000000
a[1]=1
a[0]=1
for i in range(2,n**n):
    a[i]+=a[i-1]+a[i-2]
    if(a[i]==n):
        print("Номер этого числа равен:",end="")
        print(i)
        break

    
        
