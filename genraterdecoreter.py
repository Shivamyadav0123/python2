def culculate(number):
    sum=0
    for num in number:
        sum=sum+num
    return sum
number=(10,20,30,40,50)
print(culculate(number))   


def genrater():
    yield 1
    yield 2
x=genrater()
print(next(x))
print(next(x))     

def decorater():
    a=10
    b=20
    print(a+b)
decorater()    

def a():
    return("Hello Shubh.How are you")
b=a()
print(b)
def c(a):
    print(b)

def outer():
    def inner():
        print("This is inner function")
    inner()
    print("this is a outer")
outer()

def decorater(func):
    def rappar():
        print("this is a inner function")
        func()
        print("How are you")
    return rappar
@decorater
def hello():
    print("Hello How are you")
hello()    

a=int(input("Enter the number"))
if a>0:
    print("positive number")
else:
    print("Nigetive number")    

a=10.20
b=int(a)
print(b)
print(type(b))

def decoreter():
    a=10
    b=20
    print(a+b)
decoreter()

def a(x):
    def b():
        print("before changing")
        x()
        print("After changing")

    return b
@a
def c():
    print("this is decorater function")
c() 
