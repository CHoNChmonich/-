#1
print("Введите значение N: ",end="")
n=int(input())
a=[]
b=[]
print("Заполните массив а ",n," элементами:")
for i in range(n):
    a.append(int(input()))
b.append(a[0])
for i in range(1,len(a)):
    if(a[i]!=a[i-1]):
        b.append(a[i])
print("Измененный массив а:")
print(b)

#2
print("Введите значение N:",end="")
n=int(input())
a=[]
b=[]
c=[]
print("Заполните массив",n,"элементами:",end="")
for i in range(n):
    a.append(int(input()))
for i in range(len(a)):
    counter=1
    
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            counter+=1
    if(a[i] not in c):
        c.append(a[i])
        b.append(counter)
    
for i in range(len(b)):
    if(b[i]==2):
        a.remove(c[i])
        a.remove(c[i])
print(len(a))
print(a)
#3
print("Введите значение N:",end="")
n=int(input())
a=[]
print("Заполните массив",n,"элементами:",end="")
for i in range(n):
    a.append(int(input()))
maxim=0
flag=True
c1=0
for i in range(n):
    if(flag):
        maxim=a[i]
        c1=i
        flag=False
    if(a[i]>maxim):
        maxim=a[i]
        c1=i
minim=0
flag=True
c2=0
for i in range(n):
    if(flag):
        minim=a[i]
        c2=i
        flag=False
    if(a[i]<minim):
        minim=a[i]
        c2=i
a.insert(c1+1,0)
a.insert(c2,0)
print("Измененный массив:")
print(a)
#5
print("Введите значение N:",end="")
n=int(input())
a=[]
b=[]
print("Заполните массив",n,"элементами:",end="")
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if(a[i]>0):
        b.append(i)
counter=0
for i in range(len(b)):
    a.insert(b[i]+counter,0)
    counter+=1
print("Измененный массив:")
print(a)
#4
print("Введите значение N:",end="")
n=int(input())
a=[]
b=[]
print("Заполните массив",n,"элементами:",end="")
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if(a[i]<0):
        b.append(i)
counter=0
for i in range(len(b)):
    a.insert(b[i]+1+counter,0)
    counter+=1
print("Измененный массив:")
print(a)



