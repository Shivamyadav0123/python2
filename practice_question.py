a=10
b=(float(a))
print(b)

a=int(input("Enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("Table",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

age = int(input("Enter a number"))
if age>=18:
    print("Valid")
else:
    print("Not valid")  

marks=int(input("Enter a number"))
if marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C") 
else:
    print("Fail") 


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

a=(input("Enter a number"))
fact=0
for ch in a:
    if ch.lower() in "aeiou":
        fact+=1
print(fact) 

a=lambda a:a*a
print(a(10))     

a=[1,2,3,4,5,6,7,8]
b=list(map(lambda a:a*a,a))
print(b)

a=[10,20,30,40,55,63,75]
b=list(filter(lambda a:a%2!=0,a))
print(b)

from functools import * 
a=[10,20,30,40,50]
b=reduce(lambda a,b:a+b,a)
print(b)

from functools import *
a=[20,30]
s=reduce(lambda a,b:a+b,a)
print(s)

year=int(input("Enter a year"))
if(year%4==0)and(year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("Not leap year")    

year=int(input("Enter a number"))
if (year%4==0)and(year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("Not leap year")    

a=[10,20,30,40,50]
a.append(60)
print(a)

a=[10,20,30,40,40,20]
a.pop()
print(a)

a=[10,20,30,40,40,50,40]
b=a.count(40)
print(b)

a=[10,20,30,40,50]
print(min(a))

a=[10,20,50,70,90]
print(max(a))

a=[10,20,40,50]
print(len(a))

a=["Shivam","Aman","Rohit","Ram"]
b=list(filter(lambda a:a[0]=="R",a))
print(b)

a=["Shivam","Aman","Rohit","Ram"]
b=list(filter(lambda a:a[0]=="S",a))
print(b)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("Table",i)
    for j in range(1,11):
     print(i,"*",j,"=",i*j)

def add(a,b):
    print(a+b)
add(10,20)    

a=lambda a:a*a
print(a(5))

a=[10,20,30,40,50,60,70,80]
b=list(map(lambda x:x*x,a))
print(b)

a=[10,13,20,14,15,16,17,19]
b=list(filter(lambda a:a%2!=0,a))
print(b)

from functools import *
a=[10,20,30,40,50,60,70,80,90,100]
b=reduce(lambda a,b:a+b,a)
print(b)

year=int(input("Enter a year"))
if (year%4==0)and(year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("Not leap year")   

a=int(input("Enter a number"))
if a%2==0:
    print("even number") 
else:
    print("odd number")    

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

a=10
b=float(a)
print(b)

a=10  #not change value integer to string
b=str(a)
print(b)

a=(10,20,30,40,50) #tuple inmutable collection
a.append(60)
print(a)

a={10,20,30,40,50,60,70}
b={70,80,90,100,110,120}
c=a.union(b)
print(c)

a={10,20,30,40,50,60,70}
b={70,80,90,10,110,120}
c=a.intersection(b)
print(c)

a={10,20,30,40,50,60,70}
b={70,80,90,100,110,120}
c=a.difference(b)
print(c)

a={10,20,30,40,50,60,70}
b={70,80,90,100,110,120}
c=a.symmetric_difference(b)
print(c)

dic={
    "name":"Shivam",
    "Age":20,
    "District":"Hardoi"
}
print(dic)

dic={
    "name":"Shivam",
    "Age":20,
    "District":"Hardoi"
}
dic.update({"Age":25})
print(dic)

dic={
    "name":"Shivam",
    "Age":20,
    "District":"Hardoi"
}
dic.update({"name":"Shivam yadav"})
print(dic)

a=int(input("Enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("Table",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

a=int(input("Enter a number"))
if a%2==0:
    print("Even number")
else:
    print("odd number")    

a=[10,20,30,40,50]
a.append(60)
print(a)

a=10
b=float(a)
print(b)

a="Shivam"
b=bool(a)
print(b)

a=10
b=20
print("a+b",a+b)
print("a-b",a-b)
print("a*b",a*b)
print("a%b",a%b)

a=100
b=20
if a>b:
    print("a is grater")
else:
    print("b is grater")    

year=int(input("Enter a year"))
if(year%4==0)and(year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("not leap year")    

s="abcdefghij"
print("h" in s)

s="abcdefghij"
print("k" in s)

a,b=100,50
x=60 if a>b else 40
print(x)

count=0
while count<4:
    print(count)
    count+=1

count=1
while count<11:
    print(count)
    count+=1

a=int(input("Enter a number"))
count=1
for i in range(1,a+1):
    count*=i
print(count)

a=int(input("Enter a number"))
count=1
for i in range(1,a+1):
    count*=i
print(count)    

s=lambda a:a*a*a
print(s(3))

a=[2,3,4,5,6,7,8]
s=list(map(lambda a:a*2,a))
print(s)

a=[2,3,4,5,6,7,8,9,10]
s=list(filter(lambda a:a%2!=0,a))
print(s)

a=[10,20,13,45,17,40]
s=list(filter(lambda a:a%2==0,a))
print(s)

from functools import *
a=[10,20,30,40,50,79,48,19,39,49]
s=reduce(lambda a,b:a+b,a)
print(s) 

a=[1,3,4,7,5,2,6,8]
print(sorted(a))

age=int(input("Enter a number"))
if age>=18:
  print("Valid")
else:
  print("Invalid")  

marks=int(input("Enter the marks"))
if marks>=90:
    print("A++")
elif marks>=85:
    print("A+") 
elif marks>=80:
    print("A")  
elif marks>=75:
    print("B+")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
else:
    print("Fail")                     

def add(a,b):
    print(a+b)
add(10,30)    

a=10
b=200
c=30
d=40
b="a is grater"if a>b and a>c else "b is grater"if b>c else "c is grater"if c>d else "d is grater"
print(b)

a=int(input("Enter a number"))
for i in range(1,11):
 print(a,"*",i,"=",a*i)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("Table",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

a={10,20,30,40,50}
b={10,60,70,80,40}
s=a.union(b)
print(s)

a={10,20,30,40,50,60}
b={10,20,49,39,15,20}
s=a.intersection(b)
print(s)

a={10,20,30,40,50,60}
b={10,20,49,39,15,20}
s=a.difference(b)
print(s)

a={10,20,30,40,50,60}
b={10,20,49,39,15,20}
s=a.symmetric_difference(b)
print(s)

a=int(input("Enter the number"))
if a%2==0:
    print("even number")
else:
    print("odd number")    

a=(input("Enter a letter"))
fact=0
for ch in a:
    if ch.lower() in "aeiou":
        fact+=1
print(fact)    

a=(input("Enter a letter"))
fact=0
for ch in a:
    if ch.lower() in "aeiou":
        fact+=1
print(fact)        

a=(input("Enter a letter"))
fact=0
for ch in a:
    if ch.lower() in "aeiou":
        fact+=1
print(fact)        

a=int(input("Enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

a=int(input("Enter a number"))
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)

a="avcdsert"
for i in a:
    print(i)

for i in range(1,11):
    if i==5:
        break
print(i)    

for i in range(1,11):
    if i==5:
        continue
print(i)    


for i in range(1,21):
    if i==5:
        continue
print(i)    

a="Shivam yadav"
print(a)
print(type(a))

a={10,20,30,40,50,60,70}
b={20,30,40,50,60,70,80}
s=a.union(b)
print(s)
c=a.intersection(b)
print(c)
d=a.difference(b)
print(d)
f=a.symmetric_difference(b)
print(f)

a={10,20}
print(type(a))

a={10,20,30,40}
a.add(50)
print(a)

a={10,20,30,40,50}
s=[60,70,80,90]
a.update(s)
print(a)

try:
    a=10
    b=5
    print(a/b)
except:
    print("Thank you") 
finally:
    print("very good")    


try:
    a=10
    b=0
    print(a/b)
except Exception as e:
    print("error",e) 

class student:
    branch="CSE"
def __init__(self,name,age):
    self.name="Shivam"
    self.age=20
s=student()  
print(s)      