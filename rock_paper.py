import random
print("WELCOME TO THE GAME OF ROCK PAPER AND SICISSOR")
a=(input("ENTER YOUR CHOICE:"))
list=['r','p','s']
b=random.choice(list)
print("COMPUTER CHOICE:",b)
if(a==b):
    print("DRAW!!!")
elif(a=='r'):
    if(b=='p'):
        print("OOPS!!!!COMPUTER WINS")
    elif(b=='s'):
        print("GREAT YOU WIN")
elif(a=='p'):
    if(b=='r'):
        print("GREAT YOU WIN")
    elif(b=='s'):
        print("OOPS!!!!COMPUTER WINS")
elif(a=='s'):
    if(b=='p'):
        print("GREAT YOU WIN")
    elif(b=='r'):
        print("OOPS!!!!COMPUTER WINS")
