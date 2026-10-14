age=11
if age>=18:
    print("valid vote")

num=23
if num%2==0:
    print("num is even")
else:
    print("num is odd")  

marks=int(input("Enter a marks"))
if marks>90:
    print("A+")
elif marks>80:
    print("A")  
elif marks>70:
    print("B") 
elif marks>60:
    print("C") 
else:
    print("fail")


a=10
b=120
c=15
if a>b and a>c:
    print("A is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater") 

age=int(input("Enter your age"))
if age>=18:
    voterid=input("Enter your age")
    if(voterid=="yes"):
        print("you can vote")
    else:
        print("you cannot vote create voterid")
else:
    print("you cannot vote you are under age")     

year=int(input("Enter your year")) 
if (year%4==0)and(year%100!=0)or(year%400==0):
    print("leap year")  
else:
    print("not leap year")    

for i in range(2,100,2):
    print(i)

a=int(input("Enter a number"))
for i in range(1,a+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

i=1
while i<=10:
    print(i)
    i+=1


num=int(input("Enter a number"))
count=0
if (num<=1):
    count=count+1
else:
    for i in range(2,num):
        if (num%i==0):
         count=count+1
if count==0:
    print("prime number")
else:
    print("not prime num")                


i=1
while i<=10:
    print(i)

    i+=1

for i in range(1,40):
    print(i)
    if i==20:
        break

for i in range(1,6):
    if i==3:
        continue
    print(i)
