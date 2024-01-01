import random
a=int(input("enter the number of digits:"))
b=int(input("enter the number of alphabet:"))
c=int(input("enter the number of symbol:"))
list=[]
password=""
list2=['!','@','#','$','%','^','&','*','(',')','<','>',';','?']
for i in range(c):
    element2=random.choice(list2)
    list.append(element2)
for i in range(a):
    element=random.randint(0,9)
    list.append(element)
list3=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','Q','W','E','R','T','Y','U','I','O','P','S','D','F','G','H','J','K','L','Z','X']
for i in range(b):
    element3=random.choice(list3)
    list.append(element3)
random.shuffle(list)
for i in list:
    password=password+str(i)
print(password)
