import random
import os
print("welcome to the world of bid ")
list=["car","lcd","fridge","ring","gold chain"]
a=random.choice(list)
print(f"your item for bid is {a}")
print("enter your information here")
dict={
}
def fun():
    name=input("enter the name:")
    bid=int(input("enter the bid:"))
    dict[name]=bid
    b=input("type 'yes' if more person taking part else 'no' ")
    if(b=='yes'):
        os.system('cls')
        fun()
fun()
max=0
winner=''
for i in dict.keys():
    if(max<dict[i]):
        max=dict[i]
        winner=i
print(f"the winner is {winner} with a bid of {max} and the {a} win by  {winner}")

