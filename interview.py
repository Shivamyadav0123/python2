a=5
b=float(a)
print(b)

a=10.5
b=int(a)
print(b)
print(type(b))

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
    fact=fact*i
print(fact)    

#list
a=[10,20,30,40,50]
a.append(60)
print(a)

a=[10,20,30,40,50]
a.extend([60,70])
print(a)

a=[10,20,30,40,50]
a.extend([60,70])
print(a)

a=[10,20,30,40,50]
a.insert(0,5)
print(a)


a=[10,20,30,40,50]
a.remove(10)
print(a)


a=[10,20,30,40,50]
a.pop(0)
print(a)


a=[10,20,30,40,50]
a.clear()
print(a)


a=[10,20,30,40,50]
b=a.index(50)
print(b)


a=[10,20,30,40,50,20,50,40]
b=a.count(50)
print(b)


a=[10,20,30,40,50,2,3,4,5]
a.sort()
print(a)

#set
a={10,20,30,40,50}
b={60,70,80,90,100}
c=a.union(b)
print(c)

a={10,20,30,40,50}
b={60,20,80,40,100}
c=a.intersection(b)
print(c)

a={10,20,30,40,50}
b={60,20,80,40,100}
c=a.difference(b)
print(c)

a={10,20,30,40,50}
b={60,20,80,40,100}
c=a.symmetric_difference(b)
print(c)

#tuple
a=(10,10,20,30,40,50)
b=a.count(10)
print(b)

a=(10,10,20,30,40,50)
b=a.index(10)
print(b)

a=(10,20,30,40,50)
print(min(a))

a=(10,20,30,40,50)
print(max(a))

a=(10,20,30,40,50)
print(len(a))

a=(10,20,30,40,50)
print(sum(a))

s={
    "name":"Shivam",
    "age":20,
    "District":"Hardoi"
}
s.keys()
print(s)

s={
    "name":"Shivam",
    "age":20,
    "District":"Hardoi"
}
s.values()
print(s)

