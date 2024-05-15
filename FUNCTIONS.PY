#Create a new function called GrossnetCalculator
#It should take 1 parameter
#Parameter 1. Gross 

#Step 1: use the key word def
#Step 2: include the function name
#Step 3: specify the parameters
#Step 4: main code
#Step 5: return value

#gross = input("Enter annual gross salary\n")
#def grossnetcalculator(gross):
   # net = (float(gross) - (0.1*float(gross)))
   # print("Net Salary is: ", net)

#gross = float(input)
#calling/using the function
#grossnetcalculator(gross)

#function 2 - calculating perimeter of a rectangle
#
#def periRectangle():
   # l = int(input ("enter length:\n"))
   # w = int(input ("enter width:\n"))
   # p = (2*l) + (2*w)
    #print("perimeter of rectangle is ",p," cm")

#call the function
#periRectangle()

#homework question
#Q1 Create a function without parameters, call this: arearectangle
#in this function ask user to enter length and width
#calculate the area and print out the result.

def AreaRectangle():
    l = int(input("enter length:\n"))
    w = int(input("enter width:\n"))
    a = (l*w)
    print("area of rectangle is ",a," square centimeters ")

AreaRectangle()