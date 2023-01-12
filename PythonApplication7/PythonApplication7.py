import random
import os
def Turn_input():
    s=int(input("Enter 1 for Rock,2 for Paper,or 3 for Scissor: "))
    s=Check_condition(s)
    s=choice(s)
    return s

def Check_condition(choice):
    while (choice>3):
        choice=Turn_input()
    else:
        return choice

def choice(int1):
    if(int1==1):
        s="Rock"
    if(int1==2):
        s="Paper"
    if(int1==3):
        s="Rock"
    return s

def win_condition_p1(s,s2):
    if(s2=="Rock"and s =="Paper"):
        return True
    if(s2=="Paper"and s=="Scissor"):
        return True
    if(s2=="Scissor"and s=="Rock"):
        return True
    else:
        return False

def draw(s,s2):
    if(s==s2):
        return True

s1=["Rock","paper","scissor"]
x=int(input("Enter the Best of rounds: "))
p1=0
p2=0
i=0
d=0

while(i<x):
    i+=1
    s2=random.choice(s1)
    s2=s2.title()
    s=Turn_input()
    os.system('cls')
    print(s)
    print(s2)
    if(win_condition_p1(s,s2)==True):
        p1+=1
        print("User winns this round!!!!")
    if(win_condition_p1(s2,s)==True):
        p2+=1
        print("Computer wins this round!!!!")
    if(draw(s,s2)==True):
        d+=1
        print("This round is a Draw!!!!")
    if((p1>x/2)or(p2>x/2)):
        break
    
if (p1>p2):
    print("User won The game!!!!")

if(p2>p1):
    print("Computer won the game!!!")

if((p1==0 and p2==0 and d>0)or(p1==p2)):
    print("The game was a draw!!!")