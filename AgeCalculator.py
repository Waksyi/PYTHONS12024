"""This program should accept an input
from user and calculate the person's AGE"""

#Step 1--> create class
class AgeCalculator:
    #Step 2--> constructor
    def __init__(self) -> None:
        pass

    #function
    def CalcMyAge(self):
        YOB = int(input("Enter your Year of Birth:\n"))
        if (YOB > 2024):
            print("Invalid Year")
        else: 
            AGE = 2024 - YOB
            print("You are ", AGE, "years wiser....")



#Object initialization
#Object name can be any name
AgeObj = AgeCalculator()

#Welcome message is an optional line of code you wish to add
print ("Welcome to my Age Calculator\n")

#use the object
AgeObj.CalcMyAge()
