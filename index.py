# easy
#Write a program to check if a given number is positive, negative, or zero.


num=int(input("enter the number :"))
if num>0:
    print("Postive")
elif num==0:
    print("zero")
else:
    print("Negtive")

#Determine if a number is odd or even.

num=int(input("Enter the number:"))
if num%2==0:
    print("Even")
else:
    print("Odd")
print("even") if num%2==0 else print("odd")

#Check if a person is eligible to vote (age >= 18).


age=int(input("Enter the age:"))
if age>=18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote")

#Write a program to find the greatest of two numbers


num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
if num1>num2:
    print("num1 is greatest")
else:
    print("num2 is greatest")

#Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail."


score=int(input("Enter the marks:"))
if score>40:
    print("Pass")
# else:
    print("fail")
print("Pass") if score>40 else print("fail")     


"""Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.)."""


day=int(input("Enter the number:"))
if day==1:
    print("Monday")
elif day==2:  
    print("Tuesday")
elif day==3:  
    print("Wednesday")
elif day==4:  
    print("Thursday")
elif day==5:  
    print("Friday")
elif day==6:  
    print("Saturday")
elif day==7:  
    print("Sunday")
else:
    print("Invalid day")
    
#Implement a simple calculator to perform addition, subtraction, multiplication, and division.

operation=input("Enter operation to perform : ")
op1=float(input("Enter the number1 :"))
op2=float(input("Enter the number2 :"))
if operation=="add" or operation=="+":
    print(op1+op2)
elif operation=="sub" or operation=="-":
    print(op1-op2)
elif operation=="mul"or operation=="*":
    print(op1*op2)
elif operation=="div"or operation=="/":
    if op2==0:
        print("Division by zero is not possible")
    else:
        print(op1/op2)
else:
    print("Invalid operation")


#Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).

month=int(input("enter a month: "))
if month == 1:
        print("January")
elif month == 2:
        print("February")
elif month == 3:
        print("March")
elif month == 4:
        print("April")
elif month == 5:
        print("May")
elif month == 6:
        print("June")
elif month == 7:
        print("July")
elif month == 8:
        print("August")
elif month == 9:
        print("September")
elif month == 10:
        print("October")
elif month == 11:
        print("November")
elif month == 12:
        print("December")
else:
    print("Invalid Month")

    
#medium

#Write a program to find the greatest of three numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("The greatest number is first number")
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is second number")
else:
    print("The greatest number is third number")

#Check if a year is a leap year.

year=int(input("Enter an year :"))
print(year,"is a leap year") if (year%4==0 and year%100!=0) or (year%400==0) else print(year,"is not a leap year")


#Write a program to classify a character entered by the user as a vowel, consonant, or neither.


user_input=input("Enter a single Character :").lower()
if len(user_input)!=1:
    print("Invalid")
else:
    if user_input in['a','e','i','o','u']:
        print("Vowels")
    elif user_input.isalpha():
        print("consonant")
    else:
        print("Special characters")

#Calculate the grade of a student based on the marks they score:
1. 90-100: Grade A
2. 80-89: Grade B
3. 70-79: Grade C
4. <70: Fail."""

marks=int(input("enter student marks : "))
if marks<=100:
    if marks>=90 and marks<=100:
        print("Grade-A")
    elif marks>=80 and marks<=89:
        print("Grade-B")
    elif marks>=70 and marks<=79:
        print("Grade-C")
    else:
        print("Fail")
else:
    print("enter valid marks")

#Write a program to check if three sides length form a valid triangle.

s1 = float(input("Enter the first side length : "))
s2 = float(input("Enter the second side length : "))
s3 = float(input("Enter the third side length : "))
if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
    print("The given sides form a valid triangle.")
else:
    print("The given sides do not form a valid triangle.") 
