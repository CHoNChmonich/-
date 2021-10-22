#1
a=[]
counter=1
n=int(input())
for i in range(n):
    a.append(input())
b=[]
c=[]
k=0
c.append(a[k])
b.append(1)
for i in range(1,n):
    if(a[i]==a[i-1]):
        b[k]+=1
    else:
        k+=1
        b.append(1)
        c.append(a[i])

        
print(a)
print(b)
print(c)
#2
a=[]
counter=1
l=int(input())
n=int(input())
for i in range(n):
    a.append(input())
b=[]
c=[]
k=0
c.append(a[k])
b.append(1)
for i in range(1,n):
    if(a[i]==a[i-1]):
        b[k]+=1
    else:
        if(b[k]>l):
            b[k]=1
            c[k]=0
        k+=1
        b.append(1)
        c.append(a[i])       
print(a)
print(b)
print(c)
#3
a=[]
k=int(input())
counter=1
n=int(input())
for i in range(n):
    a.append(input())
b=[]
c=[]
j=0
c.append(a[j])
b.append(1)
for i in range(1,n):
    if(a[i]==a[i-1]):
        b[j]+=1
    else:
        j+=1
        b.append(1)
        c.append(a[i])
print(a)
print(b)
print(c)
c[k-1],c[j]=c[j],c[k-1]
b[k-1],b[j]=b[j],b[k-1]
l=[]
for i in range(len(c)):
    for j in range(b[i]):
        l.append(c[i])

print(a)
print(b)
print(c)
print(l)
#4
n=int(input())
ans=[0]*2
maxim=0
for i in range(n):
    x,y=[int(s) for s in input().split()]
    if(y>=0)and(x<0):
        if(x**2+y**2 > maxim):
            maxim=x**2+y**2
            ans[0]=x
            ans[1]=y
print(ans)
#5
import math
n=int(input())
a=[]
for i in range(n):
    a.append([])
    for j in range(2):
        a[i].append(int(input()))
        
p=0
pmax=0
p1=0
p2=0
p3=0
for i in range(n):
    for i2 in range(i+1,n):
        for i3 in range(i2+1,n):
            p=0
            p+=math.sqrt((a[i][0]-a[i2][0])**2+(a[i][1]-a[i2][1])**2)
            p+=math.sqrt((a[i][0]-a[i3][0])**2+(a[i][1]-a[i3][1])**2)
            p+=math.sqrt((a[i2][0]-a[i3][0])**2+(a[i2][1]-a[i3][1])**2)
            if(p>pmax):
                pmax=p
                p1=i
                p2=i2
                p3=i3
print(pmax,p1,p2,p3)
