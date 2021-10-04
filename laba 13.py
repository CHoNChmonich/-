#1
print("Введите стоимость 1 киллограма конфет:",end="")
x=int(input())
for i in range(10):
    print(x*i/10)
print(x)
#2
print("Введите число N:",end="")
n=int(input())
k=1
for i in range(10,10*n+1):
    k*=k*(i/10)
print(k)
#3
print("Введите число N:",end="")
n=int(input())
summ=0
for i in range(2*n):
    if(i%2!=0):
        summ+=i
print("N**2 =",end="")
print(summ)
#4
print("ВВедите число А:",end="")
a=int(input())
print("Введите число N:",end="")
n=int(input())
s=0
for i in range(n+1):
    k=a**i
    s+=k
print("Значение выражения равно:",end="")
print(s)
#5
print("ВВедите число А:",end="")
a=int(input())
print("Введите число N:",end="")
n=int(input())
s=0
for i in range(n+1):
    k=((-1)**i)*a**i
    s+=k
print("Значение выражения равно:",end="")
print(s)
