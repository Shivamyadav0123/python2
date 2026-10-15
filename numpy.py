import numpy as np
marks=np.array([10,20,30,40,50])
a=marks+10
print(a)

a=int(input("Enter a number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("Table",i)
    for j in range(1,11):
     print(i,"*",j,"=",i*j)

a=int(input("Enter a number"))
for i in range(1,a+1):
    print("Table",i)
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

a=int(input("Enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

a=lambda x:x*x
print(a(5))

a=[1,2,3,4,5]
b=list(map(lambda x:x*x,a))
print(b)

a=[1,2,3,4,5]
b=list(filter(lambda x:x%2==0,a))
print(b)

import functools as f
a=[1,2,3,4,5]
b=f.reduce(lambda x,y:x+y,a)
print(b)

