import random
import time
a=random.randint(1,50)
print("let me think of a number between 1 to 50")
time.sleep(6)
print("i am ready")
level=input("enter the level 'hard' OR 'easy':")
if(level=="easy"):
    print("you have 10 attempts to guess the number")
    chance=10
    while chance>0:
        c=int(input("guess the number:"))
        if(c==a):
            print("your guess is correct")
            break
        elif(c>a):
            print("your guess is too high")
        elif(c<a):
            print("your guess is too low")
        chance-=1
        if(chance==0):
            print("you lose!!!!!!")
if(level=="hard"):
    print("you have 5 attempts to guess the number")
    chance=5
    while chance>0:
        c=int(input("guess the number:"))
        if(c==a):
            print("your guess is correct")
            break
        elif(c>a):
            print("your guess is too high")
        elif(c<a):
            print("your guess is too low")
        chance-=1
        if(chance==0):
            print("you lose!!!!!!")