#1
print("Введите значение N:",end="")
n=int(input())
a=[]
b=[]
for i in range(n):
    print("элемент в массив а:")
    a.append(int(input()))
    print("элемент в массив b:")
    b.append(int(input()))
m=[0]*n
for i in range(n):
    m[i]=a[i]
for i in range(n):
    a[i]=b[i]
    b[i]=m[i]
print("Вывод массивa a:")
print(a)
print("вывод массива b:")
print(b)
#2
print("Введите значение N:",end="")
n=int(input())
a=[]
b=[0]*n
print("заполните массив а ",n," элементами")
for i in range(n):
    a.append(int(input()))
for i in range(n):
    s=0
    k=0
    for j in range(i+1):
        s+=a[j]
        k+=1
    b[i]=s/k
print("Массив B:")    
print(b)
#3
print("ВВедите значение N:",end="")
n=int(input())
a=[]
k=0
print("заполните массив а ",n," элементами")
for i in range(n):
    a.append(int(input()))
for i in reversed(range(n)):
    if(a[i]%2!=0):
        k=a[i]
        break
for i in range(n):
    if(a[i]%2!=0):
        a[i]=a[i]+k
print("Изменненый массив:")
print(a)
#4
print("Введите значение N:",end="")
n=int(input())
minim=0
count1=0
flag=True
a=[]
print("Заполните массив размера N:")
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if(flag):
        minim=a[i]
        count1=i
        flag=False
    if(a[i]<minim):
        minim=a[i]
        count1=i
maxim=0
flag=True
count2=0
for i in range(n):
    if(flag):
        maxim=a[i]
        count2=i
        flag=False
    if(a[i]>maxim):
        maxim=a[i]
        count2=i
c1,c2=max(count1,count2),min(count1,count2)
for i in range(c2+1,c1):
    a[i]=0
print("Измененный массив")
print(a)
#5
print("ВВедите значение N:",end="")
n=int(input())
a=[]
print("Заполните массив размера N, так чтобы все кроме первого элмента были упорядочена по возрастанию:")
for i in range(n):
    a.append(int(input()))

for i in range(1,n):
    if(a[i-1]>a[i]):
        a[i-1],a[i]=a[i],a[i-1]
print("Измененный массив:")
print(a)
    

        
    
