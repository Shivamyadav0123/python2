a=10
b=complex(a)
print(b)

a=int(input("Enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("Table",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

a=int(input("Enter a number"))
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)

a=int(input("Enter a number"))
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)  

a=int(input("Enter anumber"))
if a%2==0:
    print("Even number") 
else:
    print("Odd number")   

a=[10,20,30,40,50]
a.append(60)
print(a)

a=[10,20,30,40,50]
a.copy()
print(a)

a=[10,20,30,40,50,50,20]
b=a.count(50)
print(b)

a=[10,20,30,40,50]
b=a.index(50)
print(b)

a=[10,20,30,40,50]
a.pop()
print(a)

a=[20,10,40,30,50]
a.sort()
print(a)

a=[10,20,30,40,50]
a.clear()
print(a)

age=int(input("Enter a number"))
if age>=18:
    print("valide")
else:
    print("Not valide")     

a={10,20,30,40}
b={50,60,30,10}
v=a.union(b)
print(v)

a={10,20,30,40}
b={50,60,30,10}
v=a.intersection(b)
print(v)

a={10,20,30,40}
b={50,60,30,10}
v=a.difference(b)
print(v)

a={10,20,30,40}
b={50,60,30,10}
v=a.symmetric_difference(b)
print(v)

dic={
    "Namne":"Shivam",
    "Age":20,
    "Moble":6307577079

}
print(dic)

def add(a,b):
    print(a+b)
add(20,20)    

import calendar
year=int(input("Enter a year"))
print(calendar.calendar(year))

a=int(input("Enter a number"))
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)    

a=int(input("Enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("Table",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

year=int(input("Enter a year"))
if(year%4==0)and(year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("not leap year")  

a={10,20,30,40}
b={50,60,70,80}
c=a.union(b)
print(c)  

a={10,20,30,40}
b={10,20,70,80}
c=a.intersection(b)
print(c)

a={10,20,30,40}
b={10,20,70,80}
c=a.difference(b)
print(c)

a={10,20,30,40}
b={10,20,70,80}
c=a.symmetric_difference(b)
print(c)

a=[10,20,30,40,50]
a.append(60)
print(a)

def bb(a):
    print(a*a)
bb(10)    

b=lambda a:a*a
print(b(5)) 

a=[2,3,4,5,6,7,8,9]
b=list(map(lambda a:a*3,a))
print(b)

a=[2,3,4,5,6,7,8,9,10]
b=list(filter(lambda a:a%2==0,a))
print(b)

from functools import *
a=[10,20,30,40,50]
b=reduce(lambda a,b:a+b,a)
print(b)

a=int(input("Enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)