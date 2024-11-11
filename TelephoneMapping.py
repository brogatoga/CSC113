'''
Created on Nov 11, 2024

@author: meganbroga
Megan Broga
mfbroga2401@student.stcc.edu
Nov 11th 2024
Assignment of Chapter 4- Telephone Letter/Number Mapping
In this assignment, we will ask the user to input a character or number from the keypad,
we will find which number the character matches, then record that matching number to
tell the user which number is mapped to that character
'''
#welcome user
Title="Phone Keypad Converter"
print("Welcome to", Title)
#get input of user
char=input(str("Enter Character"))
#convert input to upper case so we can efficiently check 
char=char.upper()
status= "Phone Number Value: " 
#using reference image, check if input matches each group of characters
if char=="1":
#if it does match, add number to status
    status+="1"
elif char=="2" or char=="A" or char=="B" or char=="C":
    status+="2"
elif char=="3" or char=="D" or char=="E" or char=="F":
    status+="3"
elif char=="4" or char=="G" or char=="H" or char=="I":
    status+= "4"
elif char=="5" or char=="J" or char=="K" or char=="L":
    status+="5"
elif char=="6" or char=="M" or char=="N" or char=="O":
    status+="6"
elif char=="7" or char=="P" or char=="Q" or char=="R" or char=="S":
    status+="7"
elif char=="8" or char=="T" or char=="U" or char=="V":
    status+="8"
elif char=="9" or char=="W" or char=="X" or char=="Y" or char=="Z":
    status+="9"
elif char=="*":
    status+="*"
elif char=="0" or char== "+":
    status+="0"
elif char=="#":
    status+="#"
#if nothing matches, add question mark
else:
    status+="?"  
#print status at end  
print(status)
print("Thank you for playing",Title)
