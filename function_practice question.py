lst=[2,4,6,8,10]
square=list(map(lambda x:x*x,lst))
print(square)

#2
number=[5,10,15,20,25]
add=list(map(lambda x:x+10,number))
print(add)

#3
name=["suraj","rahul","amit","rohit"]
u=list(map(lambda x:x.upper(),name))
print(u)

#4
words=["Python","Java","JavaScript","C++"]
a=list(map(lambda a:len(a),words ))
print(a)

#5
celsius=[0,10,20,30,40]
b=list(map(lambda a:(a*9/5)+32,celsius))
print(b)

#6

number=[1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda a:a%2==0,number))
print(a)

#7
number=[5,12,8,20,15,3,25]
f=list(filter(lambda a:a>10,number))
print(f)

#8

number=[-10,5,-3,8,0,-7,12]
a=list(filter(lambda a:a>0,number))
print(a)

#9

names = ["Amit", "Rahul", "Ankit", "Suraj", "Anjali", "Rohit"]
a=list(filter(lambda a:a[0]=="A",names))
print(a)

#10

numbers=[10,12,15,18,20,23,25,30]
a=list(filter(lambda a:a%5==0,numbers))
print(a)

#11
from functools import *
numbers=[10,20,30,40,50]
s=int(reduce(lambda x,y:x+y,numbers))
print(s)

#12
from functools import *
numbers=[2,3,4,5]
s=int(reduce(lambda a,b:a*b,numbers))
print(s)

#13
from functools import *
numbers=[12,45,7,89,23,56,100]
s=int(reduce(lambda a,b:a if a>b else b, numbers))
print(s)

#14

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
s=list(filter(lambda a:a%2==0,numbers))
s1=list(map(lambda a:a*a,s))
print(s)
print(s1)

from functools import *
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
s=list(filter(lambda a:a%2==0,numbers))
s1=list(map(lambda a:a*a,s))
s2=int(reduce(lambda a,b:a+b,s1))
print(s)
print(s1)
print(s2)
