a={10,20,30,40}
b={30,40,50,60}
c=a.intersection(b)
print(c)
d=a.union(b)
print(d)
e=a.difference(b)
print(e)
f=b.symmetric_difference(a)   
print(f)

di={
    "name":"sachin",
    "age":30,
}
print(di["name"])
print(di["age"])
print(di.items())
print(di.keys())
print(di.values())
print(di.get("name"))
print(di.update({"age":31}))
print(di)
print(di.pop("age"))

a=10
b=20
print("a+b =", a+b)
print("a-b =", a-b)
print("a*b =", a*b)
print("a/b =", a/b)
print("a//b =", a//b)
print("a%b =", a%b)
#assignment operator
a=10
b=20
a+=b
print("a =", a)
print("b =", b)
print("a-b =", a-b)
print("a*b =", a*b)
print("a/b =", a/b)
#relational operator
print("a==b", a==b)
print("a!=b", a!=b)
print("a>b", a>b)
print("a<b", a<b)
print("a>=b", a>=b)
print("a<=b", a<=b)
#logical operator
print("a and b", a and b)
print("a or b", a or b)
print("not a", not a)
#membership operator
a=10
print("a in [10, 20, 30]", a in [10, 20, 30])
print("a not in [10, 20, 30]", a not in [10, 20, 30])
#identity operator
a=10
print("a is 10", a is 10)

#ternary operator
a=100
b=200
c=3000
d=100000
b="a is greatest" if a>b and a>c else "b is greatest" if b>c else "c is greatest" if c>d else "d is greatest"
print(b)

#list is a mutable and ordered or dublikate values are allowed
a=[10,20,30,40,50,10]
print(a)
#list methods
a=[10,20,30,40,50,10]
a.append(60)
print(a)

a=[10,20,30,40,50,10]
a.insert(2,25) #insert value ko diye gaye index me insert karta hai 
print(a)

a=[10,20,20,30,40,50,10]
a.remove(20) #remove method first occurance of value ko remove karta hai  
print(a)

a=[10,20,20,30,40,50,10]
a.pop(4) #pop method last value ko remove karta hai
print(a)

a=[10,20,20,30,40,50,10]
a.clear() #clear method list ke sare values ko remove karta hai
print(a)

a=[10,20,20,30,40,50,10]
a.sort() #sort method list ke values ko ascending order me sort karta hai
print(a)

a=[10,20,20,30,40,50,10]
a.reverse() #reverse method list ke values ko reverse order me sort karta hai   
print(a)

a=[10,20,20,30,40,50]
ab=a.copy()
print(ab) #copy method list ke values ko copy karta hai
print(a)

a=[10,20,20,30,40,50]
print(a.count(40)) #count method list me diye gaye value ki count ko return karta hai

#list functions
a=[10,20,20,30,40,50]
print(len(a)) #len function list ke values ki sankhya ko return karta hai

a=[10,20,20,30,40,50]
print(min(a)) #min function list ke values me se minimum value ko return karta hai

a=[10,20,20,30,40,50]
print(max(a)) #max function list ke values me se maximum value ko return karta hai

a=[10,20,20,30,40,50]
print(sum(a)) #sum function list ke values ka sum return karta hai

a=[10,20,20,30,40,50]
print(sorted(a)) #sorted function list ke values ko ascending order me sort karta hai

a=[10,20,20,30,40,50]
print(list(reversed(a))) #reversed function list ke values ko reverse order me sort karta hai

a=[10,20,20,30,40,50]
print(list(a)) #list function list ke values ko list me convert karta hai

#Dictionary in python is a collection of key-value pairs. It is mutable, unordered, and does not allow duplicate keys. Each key in a dictionary must be unique, but the values can be duplicated. 
di={
    "name":"sachin",
    "age":30,
    "city":"Delhi"
}
print(di) #printing the dictionary
print(di["name"]) #accessing value using key
print(di.get("age")) #accessing value using get() method
print(di.get("city")) #accessing value using get() method
print(di.items()) #returns a view object that displays a list of dictionary's key-value tuple pairs
print(di.keys()) #returns a view object that displays a list of all the keys in the dictionary
print(di.values()) #returns a view object that displays a list of all the values in the dictionary

#set is a collection of unordered, unique elements. It is mutable, meaning you can add or remove elements from a set. Sets are commonly used for membership testing, removing duplicates from a list, and performing mathematical operations like union, intersection, and difference.  
a={10,20,30,40}
b={30,40,50,60}
c=a.intersection(b) #intersection method returns a new set with elements that are common to both sets
print(c)

a={10,20,30,40}
b={30,40,50,60}
c=a.union(b) #union method returns a new set with all elements from both sets
print(c)

a={10,20,30,40}
b={30,40,50,60}
c=a.difference(b) #difference method returns a new set with elements that are in the first set but not in the second set
print(c)

a={10,20,30,40}
b={30,40,50,60}
c=b.symmetric_difference(a) #symmetric_difference method returns a new set with elements that are in either of the sets but not in both
print(c)

num=20
if num%2==0:
    print("num is even")
else:
    print("num is odd")    


def fectorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
a=int(input("enter the number"))
print("fectorial of",a,"is",fectorial(a))


def add(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
add(50,100,150)    

square=lambda x:x*x
print(square(5))

lst=[2,3,4,5,6,7]
result=list(map(lambda x:x*2,lst))
print(result)

lst=[2,3,4,5,6,7,8,9,10]
result=list(filter(lambda x:x%2==0,lst))
print(result)

from functools import reduce
lst=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,lst)
print(result)

a=[10,20,30]
def add(x):
    return x*x
b=list(map(add,a))
print(b)

a=[50,60,140,521]
def add(x):
    if x>120:
        return x
    return None
ax=list(map(add,a))
aaa=[]
for i in ax:
    if i is not None:
         aaa.append(i)
print(aaa)      


a=[110,124,123,54,65]
def add(x):
    return x>120
ax=list(filter(add,a))
print(ax)   

from functools import *
a=[10,20,30,40,50,60,70]
ax=int(reduce(lambda x,y:x+y,a))
print(ax) 

#ecseption error

try:
    a=10
    b=0
    print(a/b)
except:
    print(" ")
    print("Hello world")   
 



try:
    a=10
    b=0
    print(a/b)
except:
    print(" ")
    print("Hello world")
finally:
    print("Thank you shubh")   

lst=[2,4,6,8,10]
square=list(map(lambda x:x*x,lst))
print(square)