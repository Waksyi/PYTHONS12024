1.#constructors
#objects
#encapsulation
#polymorphism
#inheritance

#rule 1: create constructor 
#aka unit method (function)
#before creating objects

#creating first class that contains functions we can use to update perimeter
import math #modules or predefined code
class PerimeterBox :
    #create constructor before function
    def __init__(self) -> None:
        pass

    #second function
    def PeriRectangle(self):
        l = int(input("enter length:\n"))
        w = int(input ("enter width:\n)"))
        p = 2*l + 2*w
        print ("perimeter of rectangle is:",p, "cm")

    #third function-->perisquare
    def PeriSuare(self):
        l = int(input("Enter length:\n"))
        p = 4*l
        print ("perimeter of square is:",p,"cm")

    #fourth function-->peritriangle
    def PeriTriangle(self):
        l = int(input("Enter lenght:\n"))
        p = 3*l
        print ("Perimeter of Triangle is: ",p, "cm")

    #fifth function-->circle
    def CCircumference(self):
        r = int(input("Enter radius:\n"))
        c = 2* math.pi *r
        print ("Circumference of circle is:" ,c, "cm")
#initialize objects
periObj = PerimeterBox()
#user choice
print("Welcome to the perimeterbox\n")
print("Choose which object to calculate its perimeter:\n")
choice = int(input(" 1.Rectangle\n 2.Square\n 3.Triangle\n 4.Circle\n"))

#calling using object
#periObj.PeriRectangle()

#if statement
if choice == 1:
    periObj.PeriRectangle()
if choice == 2:
    periObj.PeriSuare()
elif choice== 3:
    periObj.PeriTriangle()
elif choice== 4:
    periObj.CCircumference()
else:
    print("invalid option")

