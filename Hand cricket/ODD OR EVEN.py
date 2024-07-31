from random import randint
from random import choice


def user_batting(total):
    
    while (1):
        print("Enter number : ",end='')
        n=int(input())
        while n>6 or n<0:
            print("INVALID CHOICE OF NUMBER")
            print("Enter Number : ")
            n=int(input())
        nn=randint(0,6)
        print("YOU : ",n,end=' ')
        print("BOT : ",nn)
        if n==nn:
            print("Batsmen Out")
            print("Total : ",total)
            break
        else:
            if n==0:
                total+=nn 
            else:
                total+=n
    return total


def userbatting(btotal,total):
    
    while (1):
        print("Enter number : ",end='')
        n=int(input())
        while n>6 or n<0:
            print("INVALID CHOICE OF NUMBER")
            print("Enter Number : ")
            n=int(input())
        nn=randint(0,6)
        print("YOU : ",n,end=' ')
        print("BOT : ",nn)
        if n==nn:
            print("Batsmen Out")
            print("Total : ",total)
            print()
            print()
            if btotal==total:
                print("!!!MATCH DRAWN!!!")
            else:
                print("!!!BOT WINS!!!")
            break
        else:
            if n==0:
                total+=nn 
            else:
                total+=n
        if btotal<total:
            print()
            print()
            print("!!!USER WINS!!!")
            break
    

def user_bowling(total):
    
    while (1):
        nn=randint(0,6)
        print("Enter number : ",end='')
        n=int(input())
        while n>6 or n<0:
            print("INVALID CHOICE OF NUMBER")
            print("Enter Number : ")
            n=int(input())
        print("BOT : ",nn,end=' ')
        print("YOU : ",n)
        if n==nn:
            print("Bot Out")
            print("Total : ",total)
            break
        else:
            if nn==0:
                total+=n
            else:
                total+=nn
    return total
        

def userbowling(utotal,total):
    total=0
    while (1):
        nn=randint(0,6)
        print("Enter number : ",end='')
        n=int(input())
        while n>6 or n<0:
            print("INVALID CHOICE OF NUMBER")
            print("Enter Number : ")
            n=int(input())
        print("BOT : ",nn,end=' ')
        print("YOU : ",n)
        if n==nn:
            print("Bot Out")
            print("Total : ",total)
            print()
            print()
            if utotal==total:
                print("!!!MATCH DRAWN!!!")
            else:   
                print("!!!USER WINS!!!")
            break
        else:
            if nn==0:
                total+=n
            else:
                total+=nn
        if utotal<total:
            print()
            print()
            print("!!!BOT WINS!!!")
            break


s=input("ODD OR EVEN : ").strip()
choicee=""
if s.lower()=="odd":
    choicee='odd'
else:
    choicee='even'
print("Enter Number : ")
n=int(input())
while n>6 or n<0:
    print("INVALID CHOICE OF NUMBER")
    print("Enter Number : ")
    n=int(input())
nn=randint(0,6)
s1=n+nn;s1ans=""
if s1%2==0:
    s1ans="even"
else:
    s1ans="odd"
print(n,'+',nn,'= ',s1ans)
userscore=0
botscore=0
if choicee==s1ans:
    print(choicee,"wins")
    option=input("BAT OR BOWL : ").strip()
    q=option.lower()
    if q=='bat' or q=='batting':
        userscore=user_batting(userscore)
        print("NOW BOT BATTING")
        userbowling(userscore,botscore)
    else:

        botscore=user_bowling(botscore)
        print("NOW USER BATTING")
        userbatting(botscore,userscore)
else:
    option=choice(["bat","bowl"])
    if option=='bat':
        print("NOW BOT BATTING")
        botscore=user_bowling(botscore)
        print("NOW USER BATTING")
        userbatting(botscore,userscore)
    else:
        print("NOW USER BATTING")
        userscore=user_batting(userscore)
        print("NOW BOT BATTING")
        userbowling(userscore,botscore)

    
    
