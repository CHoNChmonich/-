#1
a=[]
print("Введите значение N:",end="")
n=int(input())
print("Заполните массив а ,",n," элементами")
for i in range(n):
    a.append(int(input()))
print("Введите значение K:",end="")
k=int(input())
print("Введите значение L:",end="")
l=int(input())
s=0
for i in range(k,l+1):
    s+=a[i]
print("Среднее арифметическое равно:")
print(s/(l-k+1))
#2
a=[]
print("Введите значение N:",end="")
n=int(input())
flag=True
print("заполните массив а ",n," элементами")
for i in range(n):
    a.append(int(input()))
for i in range(1,n-1):
    if(a[i]-a[i-1]==a[i+1]-a[i]):
        
        ans=a[i]-a[i-1]
    else:
        flag=False
        break
if(flag):
    print(ans)
else:
    print("0")
#3
a=[]
flag=False
minim=0
print("Введите значение N:",end="")
n=int(input())
print("Заполните массив а ",n," элементами")
for i in range(n):
    a.append(int(input()))
for i in range(2,n,2):
    if(flag==False):
        minim=a[i]
        flag=True
    if(a[i]<minim):
        minim=a[i]
print("Минимальный элемент равен:")
print(minim)
#4
maxim=0
print("Введите значение N:",end="")
n=int(input())
print("Заполните массив а ",n," элементами")
a=[]
for i in range(n):
    a.append(int(input()))
for i in reversed(range(1,n-1)):
    if(a[i]>a[i+1])and(a[i]>a[i-1]):
        maxim=a[i]
        break
print("Последний локальный максимум равен:")
print(maxim)
#5
print("ВВедите значение N:",end="")
n=int(input())
a=[]
n1=0
n2=0
print("Заполните массив а ",n," элементами")
for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(i+1):
        if(a[i]==a[j]):
            n1=i
            n2=j
            break
maxim=max(n1,n2)
minim=min(n1,n2)
print("Номера совпадающих элементов:")
print(minim,maxim)
    
