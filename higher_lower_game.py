import random
import higher_lower_database as hld
score=0
while(score>=0):
    dict1=random.choice(hld.list)
    dict2=random.choice(hld.list)
    print(f"compare 1: {dict1['name']},{dict1['work']},{dict1['country']}")
    print("                VS              ")
    print(f"compare 1: {dict2['name']},{dict2['work']},{dict2['country']}")
    choice=int(input("who has more follower? type 1 or 2 or 0 if both has same follower"))
    if(choice==1):
        if(dict1['follower']>dict2['follower']):
            score+=1
            print("correct answer")
            print("your score is",score)
            print("your next question is ")
        else:
            print("incorrect answer")
            print("your score is ",score)
            break
    if(choice==2):
        if(dict1['follower']<dict2['follower']):
            score+=1
            print("correct answer")
            print("your score is",score)
            print("your next question is ")
        else:
            print("incorrect answer")
            print("your score is ",score)
            break
    if(choice==0):
        if(dict1['follower']==dict2['follower']):
            score+=1
            print("correct answer")
            print("your score is",score)
        else:
            print("incorrect answer")
            print("your score is ",score)
            break
