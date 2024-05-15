"""Database Management Class - Python Programming Module Assignment #1
Part 1 (*/19)
● Based on the notes of classes uploaded here and the class exercise covered on Friday
(10th/05/24) in class
Create a new Python file called Assignment1. On this file, do the following:"""
#1. Create a class called AreaBox

import math
class AreaBox:
    def __init__(self) -> None:
        pass

#2. This class should contain a constructor and 3 functions.

#3. Function one (1) is to be called AreaRectangle. It should calculate the area of a
#Rectangle. This function should ask the user to input the Length and Width of the
#Rectangle before displaying the output.
    def AreaRectangle(self):
        l = int(input("Enter Length:\n"))
        w = int(input("Enter Width:\n"))
        a = l*w
        print("Area of Rectangle is: ", a , "cm squared")

#4. Function two (2) is to be called AreaTriangle. It should calculate the area of a Triangle.
#This function must ask the user to input the Base and Height of the triangle first before
#displaying the output.

    def AreaTriangle(self):
        b = int(input("Enter Base:\n"))
        h = int(input("Enter Height:\n"))
        a = (b*h)/2
        print("Area of Triangle is " ,a, "cm squared")

#5. Function three (3) is to be called AreaCircle. It should calculate the area of a Circle.
#This function must ask the user to input the circle's radius before displaying the output.
#Use the pi from the module math.

    def AreaCircle(self):
        r = int(input("Enter Radius:\n"))
        a = math.pi * r*r
        print("Area of Circle is", a , "cm squared")

#6. Initialize (create 3 objects), each one will be used to access the three functions above.

ABObj = AreaBox()

print("Welcome to My Area Box!")
print("Choose which object to calculate its area")
choice = int(input(" 1.Rectangle\n 2.Triangle\n 3.Circle\n"))

if choice ==1:
    ABObj.AreaRectangle()
elif choice ==2:
    ABObj.AreaTriangle()
elif choice ==3:
    ABObj.AreaCircle()
else:
    print ("Invalid option\n")

#7. Use/invoke the objects created in Step 6.
#**Submit this python file to Google Classroom

'''Part 2 (*/6)
Based on your program in part 1, determine if the following is occurring/present in your code.
Answer Yes/No. If Yes, specify which line of code is responsible for it. State your reason
also.
2.1 Encapsulation
Yes - In line 9 when we create a class it wraps all data and function into single entity
Encapsulation protects the file and restricts access to to methods and variables from 
outside which prevents data from being modified by unauthorised users

2.2 Polymorphism
Yes - polymorphism allows us to perform same action in many different ways.
Line 45 the ABObj or (Area Box Object) is an example of polymorphism where we perform the calcuation
of the area of three different objects in the same way but different functions according to their required 
mathematical formula.

2.3 Inheritance
No - inheritance applies when a child class inherits its methods and attributes from a parent class. 
The codes in this assignment simply provides the functions to calculate the are of shapes specified.

**Type your answer for Part 2 on a Word Document and submit also or type in as comments into
Part 1 Python file.

DUE DATE: Wednesday (15th May, 2024 4:10 pm)'''

