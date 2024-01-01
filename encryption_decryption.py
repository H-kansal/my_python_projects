print("type 'encrypt' for encrytion and 'decrypt' for decryption:")
a=input()
print("type your message")
b=input()
print("enter the shift: ")
c=int(input())
list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d=""
if(a=='encrypt'):
    for i in b:
        if i in list:
            y=26-(list.index(i)+c)
            d=d+list[-y]
        else:
            d=d+i
print(d)
if (a=='decrypt'):
    for i in b:
        if i in list:
            y=(list.index(i)-c)
            d=d+list[y]
        else:
            d=d+i
print(d)