#output
import string


FName= "Tony"
LName="Stark"
age=51
is_adult="Genius"
print(FName,LName,age,is_adult)


#input
Name=input("What is your name?")
print(Name)
heroName=input("Who is your Superhero ?")
print(heroName)



# Type Conversion
old_age=input("Enter your old_age")
new_age=int(old_age)+2
print(new_age)

#conversions
number=18
print(float(18))



# # add two numbers
num1=input("Enter the first number")
num2=input("Enter the second number")
sum=int(num1)+int(num2)
print("The sum is:", sum)


#uppercase and lower
name="AnanyA"
print(name.upper())
print(name.lower())

#finding
name="Ananya Vishnoi"
print(name.find('y'))

#replace
name="ananya"
print(name.replace('ananya','jayant'))

#finding
name="Jayant Khanna Ananya Vishnoi"
print("Jayant" in name)


#calculation
print(12-5)
print(2**3)

#Logical Operator
#OR
print(3>2 or 4<6)
print(2>4 and 6==4)
print(not 2==3)


#if-else
age=19
if age>19:
    print("You are an adult")
elif age>=10 and age<=20:
    print("Teen")
else:
    print("Wrong")    

#####################       MINI PROJECTT         ######################
####################        CALCULATOR             ######################

from re import sub


first=input("Enter First number:")
operator=input("Enter the operator +.-,*,/):")
second=input("Enter the second number: ")
if operator== "+":
    print(int(first)+int(second))
elif operator=="-":
    print(int(first)-int(second))
elif operator== "*":
    print(int(first)*int(second))
elif operator=="/":
    print(int(first)/int(second))
else:
    print("Wrong Choice!!")


#range
numbers=range(10)
print(numbers)

#loop
i=1
while i<=10:
    print(i)
    i=i+1

i=1
while i<=10:
    print(i * "*")
    i=i+1

i=10
while i>=0:
    print(i * "*")
    i=i-1  


#for loop
for item in range(10):
    print(item+1)


#list
marks=[99,98,93,90]
print(marks[0])
print(marks[3])
print(marks[-1])
print(marks[0:3])
marks.append(100)
print(marks)
marks.insert(0,80)
print(marks)

print(len(marks))
print(100 in marks)

#clear
i=0
while i<len(marks):
    print(marks[i])
    i=i+1

marks.clear()
print(marks)    