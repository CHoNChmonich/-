#1
def f(a,b):
    if(a>2)and(b<=3):
        return True
    return False
a=int(input())
b=int(input())
print(f(a,b))
#2
def f(a,b,c):
    if(a<b)and(b<c):
        return True
    return False
a=int(input())
b=int(input())
c=int(input())
print(f(a,b,c))
#3
x=int(input())
def f(x):
    c=0
    while(x>0):
        x=x//10
        c+=1
    if(c==2):
        return True
    return False
print(f(x))
#4
x=input()
x1=int(x[0])
x2=int(x[1])
x3=int(x[2])
def f(a,b,c):
    if((a<b)and(b<c))or((a>b)and(b>c)):
        return True
    return False
print(f(x1,x2,x3))
#5
x=input()
x1=int(x[0])
x2=int(x[1])
x3=int(x[2])
x4=int(x[3])
if(x1==x4)and(x2==x3):
    print("True")
else:
    print("False")
#6
a=int(input())
b=int(input())
c=int(input())
if(a**2+b**2==c**2)or(a**2+c**2==b**2)or(b**2+c**2==a**2):
    print("True")
else:
    print("False")
#7
a=int(input())
b=int(input())
c=int(input())
def f(a,b,c):
    if(a+b>c)or(a+c>b)or(b+c>a):
        return True
    return False
print(f(a,b,c))
