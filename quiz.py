import random
import quiz_database as qd
print("**********************************")
print("Welcome to quiz game")
print("**********************************")
str=random.choice(qd.list)
print(str)
answer=input()
index=qd.list.index(str)
if(answer==qd.answer[index]):
    print("you are correct")
else:
    print("your answer is incorrect")
