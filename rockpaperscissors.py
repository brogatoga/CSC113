'''
Created on Oct 31, 2024

@author: meganbroga
Megan Broga
Oct 31 2024
CSC 113
Make a rock paper scissors game
'''
print("Welcome to Rock Paper Scissors Battleground, May the odds ever be in your favor")
import random
computer=random.randint(0,2)
rock=0
paper=1
scissors=2
player= int(input("Enter [0] for rock,[1] for paper,and [2] for scissors"))

#if the player does not input a correct input
if player<rock or player>scissors:
    status= "LOSER, could not even follow a simple 1 sentence instruction"
#if the player inputs same as computer
elif player==computer:
    status= "TIE you both threw: "
    if player== rock:
        status+="rock"
    elif player==paper:
        status+="paper"
    elif player==scissors:
        status+="scissors"
#if player selects paper, check if computer = rock (win condition), if not, you lose
elif player== paper:
    if computer == rock:
        status="WINNER your paper covered the computers rock"
    else:
        status= "LOSER the computer's scissors cut your paper"
#check players win condition for selecting scissors, if not met, you lose
elif player== scissors:
    if computer== paper:
        status= "WINNER your paper cut the computers paper"
    else:status= "LOSER computers rock smashed your scissors into bits and pieces"
# check win condition for scissors, if not, player loses
else:
    if computer== scissors:
        status= "WINNER your rock smashed the computers scissors into bits and pieces"
    else:
        status= "LOSER computers paper covered your rock"

print(status)
print("Thank you for playing Rock Paper Scissors Battleground")
