'''
Created on Oct 28, 2024

Your name : Megan Broga
Email: mfbroga2401@stcc.edu
Date: Oct 28th 2024
Course Name and Number: CSC 113- Intro to Python Programming
Problem/Homework Number: Chapter 2: Initial Value of a Money Account
Short Description of the Problem: Given the final value of a bank account, the interest per
year, and the amount of years the amount will sit in the bank, we will calculate the
beginning initial deposit neededto achieve this final values in the parameters given.


@author: meganbroga
'''
final_val= float(input("Enter final account value: "))
annual_interest= float(input("Enter annual interest rate in percent: "))
years= float(input("Enter number of years: "))

#turn annual interest into monthly interest
monthly_interest= (annual_interest/100 )/12
#turn months into years
months=years*12
#find denominator of given equation, which is the rate the final value is changing by 
rate_of_change= (1+monthly_interest)**months

initialDepositAmount= final_val/rate_of_change
#print final value in 2 decimal points
print(f"Initial deposit value is {initialDepositAmount:.2f}. ")


