import random
import hungman_game_figure as figure
import hangman_game_name as name
def fun():
    print("let's play Hangman game!!!")
    a=random.choice(name.list)
    list3=[]
    for i in a:
        list3.append(i)
    print(f"your word is of {len(a)} letter, guess the lettter")
    list2=[]
    for i in range(len(a)):
     list2.append('_')
    print(list2)
    life=6
    while(life>=1):
        if(list3==list2):
            print("you win the game")
            c=input("type 'yes' if play continue if not type 'no':")
            if(c=='yes'):
                fun()
                break
            else:
                print("thanks for playing")
                break
        b= input("Guess the letter:")
        for j in range(len(a)):
            if(a[j]==b):
                print("Nice you guess the correct")
                list2[j]=b
                print(list2)
        if b not in a:
            print("oops!!!! you lose a life")
            life-=1
            if(life==0):
                print("Game over")
        print(figure.figures[life])
        if(life==0):
            d=input("type 'yes' if play continue if not type 'no':")
            if(d=='yes'):
                fun()
                break
            else:
                print("thanks for playing")  
fun()
    
    
    