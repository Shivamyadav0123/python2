#loop
i=1
while i<=10:
    print(i)
    i+=1

for i in range(10):
    if i==5:
        break
    print(i)

for i in range(10):
    if i==5:
        continue
    print(i)

#function
def aa(a,b):
    return a+b
print(aa(10,20))  

def aa(a,b):
    return a-b 
print(aa(20,10)) 

a=input("Inter a string")
print(a[::-1])

a=input("Enter a string")
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

def add(a,b):
    print(a+b)
add(10,20)    

year=int(input("Enter a year"))
if (year%4==0)and(year%100!=0)or(year%400==0):
    print("Leap year")
else:
    print("Not leap year") 

names = ["Amit", "Rahul", "Ankit", "Suraj", "Anjali", "Rohit"]  
a=list(filter(lambda a:a[0]=="A",names))
print(a)      

names = ["Amit", "Rahul", "Ankit", "Suraj", "Anjali", "Rohit"]  
a=list(filter(lambda a:a[0]=="S",names))
print(a)

a=100
b=200
c=30
d="a is greater" if a>b and a>c else "b is greater" if b>c else "c is greater"
print(d)

a=10000
b=2000
c=300
d=40
r="a is greater" if a>b and b>c else "b is greater" if b>c else "c is greater" if c>d else "d is greater"
print(r)

a=int(input("Enter a number"))
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)    