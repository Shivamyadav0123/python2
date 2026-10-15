#list is a ordered and mutable collection
a=[10,20,30,40,50,60,70,80]
print(a)
print(type(a))

#list ke method
#append
a=[20,30,40,50,60,70]
a.append(80)
print(a)

#insert
a=[20,30,40,50,60,70]
a.insert(0,10)
print(a)

#extend
a=[20,30,40,50,60,70]
a.extend([80,90])
print(a)

#remove
a=[20,30,40,50,60,70]
a.remove(20)
print(a)

#pop
a=[20,30,40,50,60,70]
a.pop()
print(a)

#clear
a=[20,30,40,50,60,70]
a.clear()
print(a)

#count
a=[20,30,40,50,60,70,20,30,50]
a.count(30)
print(a)

#reverse
a=[20,30,40,50,60,70]
a.reverse()
print(a)

#copy
a=[20,30,40,50,60,70]
b=a.copy()
print(b)

#count
a=[20,30,40,50,60,70,20,30,50]
b=a.count(40)
print(b)

#list function
a=[20,30,40,50,60,70]
print(len(a))

a=[20,30,40,50,60,70]
print(max(a))

a=[20,30,40,50,60,70]
print(min(a))

a=[20,30,40,50,60,70]
print(sum(a))

a=[20,30,40,50,60,70,50,40,30]
print(sorted(a))

#tuple is a ordered and immutable collection

a=(10,20,30,40,50,60,20)
b=a.count(20)
print(b)

a=(10,20,30,40,50,60,20)
a.index(30)
print(a)

#tuple function
a=(10,20,30,40,50,60,)
print(len(a))

a=(10,20,30,40,50,60,20)
print(min(a))

a=(10,20,30,40,50,60,20)
print(max(a))

a=(10,20,30,40,50,60,20)
print(sorted(a))

#dictionary
student={
    "name":"Shivam",
    "age":20,
    "marks":80,

}
print(student)

student={
    "name":"Shivam",
    "age":20,
    "marks":80,
}
student.keys()
print(student)

student={
    "name":"Shivam",
    "age":20,
    "marks":80,

}
student.values()
print(student)

student={
    "name":"Shivam",
    "age":20,
    "marks":80,

}
student.update({"age":25})
print(student)

i=1
while i<=10:
    print(i)
    i+=1

for i in range(10):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

def add(a,b):
    return a+b,a-b
print(add(50,20))

n=int(input("Enter the number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)   


s=input("Enter string")
print(s[::-1])     

a=[10,20,30,40,50,60,70,80,90]
print(min(a))

s=lambda x:x*x
print(s(5))

a=input("Enter string")
count=0
for ch in a:
    if ch.lower() in "aeiou":
        count+=1
print(count)   


a=input("Enter a string")
count=0
for ch in a:
    if ch.lower() in "aeiou":
     count+=1     
print(count)    

a=int(input("Enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

a=int(input("Enter a number"))
for i in range(2,a+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

a=int(input("Enter a number"))
for i in range(2,a+1):
    print("table",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

a=int(input("Enter the number"))
for i in range(2,a+1):
    print("Table",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("Table",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

lst=[2,3,4,5,6,7,8]
lst.append(10)
print(lst)

a=int(input("Enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("table",i)
    for j in range(1,11):
        print(a,"*",j,"=",i*j)

def add(a,b):
    print(a+b)
add(10,20)    

import culculete
print(culculete.add(10,20))
print(culculete.subtract(30,20))

year=int(input("Enter a year"))
if (year%4==0)and(year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("not leap year")

year=int(input("Enter the year"))
if (year%4==0)and(year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("Not leap year")        

year=int(input("Enter the year"))
if (year%4==0)and(year%100!=0)or(year%400==0):
    print("leap year")
else:
    print("Not leap year")  

names = ["Amit", "Rahul", "Ankit", "Suraj", "Anjali", "Rohit"]  
a=list(filter(lambda a:a[0]=="A",names))
print(a)

a=10
b=200
c=30
b="a is grater"if a>b and a>c else "b is grater" if b>c else "c is greter"
print(b)

a=100
b=30
c=50
d=500
b="a is greter"if a>b and a>c else "b is greter"if b>c else "c is greter" if c>d else "d is greter"
print(b)

a=100
b=30000
c=50
d=500
b="a is greatest" if a>b and a>c else "b is greatest" if b>c else "c is greatest" if c>d else "d is greatest"
print(b)

a=[10,20,30,40,50,20,20]
print(a)
a.append(80)
print(a)

a=[10,20,30,40,50,20,20]
print(a)
c=a.count(20)
print(c)

a=int(input("Enter a number"))
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)    

a=input("Enter a string")
count=0
for ch in a:
    if ch.lower() in "aeiou":
     count+=1
print(count)    