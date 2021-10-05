#1
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(1,n):
    if(a[i]==a[i-1]):
        a.pop(a[i])
print(a)

#2
n=int(input())
a=[]
b=[]
c=[]
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



for i in range(len(c)):
    if(b[i]==2):
        a.remove(c[i])
        a.remove(c[i])
print(a)
#3
n=int(input())
a=[]

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
print(a)
#5
n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if(a[i]>0):
        b.append(i)
counter=0
for i in range(len(b)):
    a.insert(b[i]+counter,0)
    counter+=1
print(a)
#4
n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if(a[i]<0):
        b.append(i)
counter=0
for i in range(len(b)):
    a.insert(b[i]+1+counter,0)
    counter+=1
print(a)



