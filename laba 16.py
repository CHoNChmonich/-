#1
print("Введите число n:",end="")
n=int(input())
a=[]
counter=0
for i in range(1,n**2):

    if(i%2!=0):
        counter+=1
        a.append(i)
    if(counter==n):
        break
print("Первые n нечетных чисел:")
print(a)
#2
print("Введите значение N:",end="")
n=int(input())
m=[]
print("Введите значение A:",end="")
a=int(input())
print("Введите значение D:",end="")
d=int(input())
k=a
for i in range(n):
    m.append(k)
    k=k*d
print("Итоговый массив:")
print(m)
#3
print("Введите значение N:",end="")
n=int(input())
print("Введите значение A:",end="")
a=int(input())
print("Введите значение B:",end="")
b=int(input())
m=[0]*n
for i in range(n):
    if(i==0):
        m[i]+=a
    elif(i==1):
        m[i]+=b
    else:
        for j in range(i):
            m[i]+=m[j]
print("Итоговый массив:")
print(m)
#4
print("Введите значение N:",end="")
n=int(input())
a=[]
for i in range(n):
    a.append(i)
for i in range(n):
    print(a[i],a[n-i-1],end=" ")
#5
print("Введите значение N:",end="")
n=int(input())
a=[]
for i in range(n):
    a.append(i)
print("Элементы с нечетными номерами:")
for i in range(1,n,2):
    print(a[i])
print("Элементы с четными номерами в порядке убывания:")
for i in reversed(range(0,n,2)):
    print(a[i])
            
