#lambda function ek enonymous function hota hai jiska koi naam nahi hota hai
square=lambda x:x*x
print(square(5))

#map functoin ka use list ke pretek eliment operation karne ke liye hota hai
numbers=[1,2,3,4,5]
result=list(map(lambda x:x*x,numbers))
print(result)

#filter function ka use list ke pretek eliment ko filter karne ke liye hota hai
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0,numbers))
print(even_numbers)

numbers=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=list(filter(lambda x:x%2!=0,numbers))
print(odd_numbers)

#reduse functoin ka use kai values ko ek single value me reduce karne ke liye hota hai
from functools import reduce
a=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,a)
print(result)

#modules ek python file hota hai jisme functions, variables, classes hote hai jise dusre python file me import karke use kiya ja sakta hai      
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

import culculete
print(culculete.add(10,20)) 
print(culculete.subtract(20,10))

#built-in modules ek python file hota hai jisme functions, variables, classes hote hai jise dusre python file me import karke use kiya ja sakta hai
#import math
#print(math.factorial(5))#built-in modules ka use factorial nikalne ke liye hota hai

#user-defined modules ek python file hota hai jisme functions, variables, classes hote hai jise dusre python file me import karke use kiya ja sakta hai 
def add(a,b):
    print(a+b)
add(10,20)    

#positional arguments ek function me arguments ko position ke hisab se pass kiya jata hai
def student(name,age):
    print("name:",name)
    print("age:",age)
student("shubh",20)

para="shubh devansh shivam shubh shubh"
words=para.lower().split()
freq={}
for i in words:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)     


para="shubh devansh shivam "
words=para.lower().split()
freq={}
for i in words:
    for w in i:
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1    
print(freq) 

para="shubh devansh shivam "
words=para.lower().strip()
freq={}
for w in words:
    if w!=" ":
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1    
print(freq)     
# 
import os
file_name="student.txt"
def add_student():
    print("Add a new student record")
    student_name=input("Enter the student name")
    student_roll=int(input("Enter the roll number"))
    student_marks=int(input("Enter the marks"))
    marks1=int(input("Enter the marks"))
    marks2=int(input("Enter the marks"))
    marks3=int(input("Enter the marks"))

    totel=marks1+marks2+marks3
    percentage=totel/3
    if percentage>90:
        grade="A"
    elif percentage>80:
        grade="B"
    elif percentage>70:
        grade="C"
    else:
        grade="Fail"
    with open("shivam.txt","a")as file:
        file.write("student_name",+str(student_name)+"\n")
        file.write("student_roll",+str(student_roll)+"\n")
        file.write("student_marks",+str(student_marks)+"\n")
        file.write("marks1",+str(marks1)+"\n")
        file.write("marks1",+str(marks2)+"\n")
        file.write("marks1",+str(marks3)+"\n")
        file.write("totel",+str(totel)+"\n")
        file.write("percentage",+str(percentage)+"\n")
        file.write("grade",+(grade)+"\n")

def search_student():
    roll_no=input("Enter your roll number")
    with open("shivam.txt","r")as file:
     add_student(),   

