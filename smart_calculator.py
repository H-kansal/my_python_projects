exit=False
while not exit:
    a=int(input("enter the first number:"))
    old=False
    while not old:
        print("+")
        print("-")
        print("*")
        print("/")
        print("//")
        print("%")
        o=input("chose the operator")
        b=int(input("enter the second number:"))
        match(o):
            case '+':
                operation=a+b
            case '-':
                operation=a-b
            case '*':
                operation=a*b
            case '/':
                operation=a/b
            case '%':
                operation=a%b
            case '//':
                operation=a//b
            case '_':
                print("out of range")
        print(a,o,b,"=",operation)
        decide=input("type 'y' if continue with {operation} if want to start new type 'n' else 'x' " )
        if(decide=='y'):
            a=operation
        if(decide=='n'):
            old=True
        if(decide=='x'):
            old=True
            exit=True



