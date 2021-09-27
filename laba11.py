#1
a=int(input())
b=int(input())
if(a>b):
    b=a
elif(b>a):
    a=b
else:
    a=0
    b=0
print(a,b)
#2
a=int(input())
b=int(input())
c=int(input())
m=0
pm=0
if(a>b)and(a>c):
    m=a
    if(b>c):
        pm=b
    else:
        pm=c
elif(b>a)and(b>c):
    m=b
    if(a>c):
        pm=a
    else:
        pm=c
elif(c>a)and(c>b):
    m=c
    if(a>b):
        pm=a
    else:
        pm=b
else:
    m=a
    pm=b
print(m+pm)
#3
a1=int(input())
b1=int(input())
c1=int(input())
a2=int(input())
b2=int(input())
c2=int(input())
ac2=(a1-c1)**2+(a2-c2)**2
ab2=(a1-b1)**2+(a2-b2)**2
ac=ac2**0,5
ab=ab2**0,5
if(ac>ab):
    print(b1,b2,ab)
else:
    print(c1,c2,ac)
#4
x=int(input())
y=int(input())
if(x*y>0):
    if(x>0)and(y>0):
        print("1")
    else:
        print("3")
else:
    if(x<0):
        print("2")
    else:
        print("4")
#5
x=int(input())
if(x>0):
    print("положительное",end=" ")
elif(x<0):
    print("отрицательное",end=" ")
else:
    print("нулевое число",end=" ")
if(x%2==0)and(x!=0):
    print("четное число")
if(x%2!=0):
    print("нечетное число")
#6
x=int(input())
def f(x):
    c=0
    while(x>0):
        x=x//10
        c+=1
    return c
if(x%2==0):
    print("четное",end=" ")
    if(f(x)==1):
        print("однозначное число",end=" ")
    if(f(x)==2):
        print("двузначное число",end=" ")
    if(f(x)==3):
        print("трехзначное число",end=" ")
else:
    print("нечетное",end=" ")
    if(f(x)==1):
        print("однозначное число",end=" ")
    if(f(x)==2):
        print("двузначное число",end=" ")
    if(f(x)==3):
        print("трехзначное число",end=" ")

