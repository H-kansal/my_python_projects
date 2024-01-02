from coffee_machine_database import dict
milk=200
water=200
profit=0
while((milk>0 and water>0)):
    name=input("what would you like to have?(latte/cappuccino/mocha/espresso)")
    if(name=='off'):
        print("GOOD BYE")
        break
    elif(name=="system"):
        print("milk=",milk)
        print("water=",water)
        print("profit=",profit)
    elif(name=='latte'):
        if((milk<dict['latte']['milk'] and water<dict['latte']['water'])):
            print("sorry,not enough milk or water")
        elif(milk>=dict['latte']['milk'] and water>=dict['latte']['water']):
            print("please insert coin")
            f_coin=int(input("enter the 5 rupee coin:"))
            t_coin=int(input("enter the 10 rupee coin:"))
            tw_coin=int(input("enter the 20 rupee coin:"))
            change=(5*f_coin+10*t_coin+20*tw_coin)-dict['latte']['price']
            print(f"here is your{change} change")
            print(f"Here is your {name}")
            milk-=dict['latte']['milk']
            water-=dict['latte']['water']
            profit+=dict['latte']['price']
    elif(name=='mocha'):
        if((milk<dict['mocha']['milk'] and water<dict['mocha']['water'])):
            print("sorry,not enough milk or water")
        elif(milk>=dict['mocha']['milk'] and water>=dict['mocha']['water']):
            print("please insert coin")
            f_coin=int(input("enter the 5 rupee coin:"))
            t_coin=int(input("enter the 10 rupee coin:"))
            tw_coin=int(input("enter the 20 rupee coin:"))
            change=(5*f_coin+10*t_coin+20*tw_coin)-dict['mocha']['price']
            print(f"here is your{change} change")
            print(f"Here is your {name}")
            milk-=dict['mocha']['milk']
            water-=dict['mocha']['water']
            profit+=dict['mocha']['price']
    elif(name=='espresso'):
        if((milk<dict['espresso']['milk'] and water<dict['espresso']['water'])):
            print("sorry,not enough milk or water")
        elif(milk>=dict['espresso']['milk'] and water>=dict['espresso']['water']):
            print("please insert coin")
            f_coin=int(input("enter the 5 rupee coin:"))
            t_coin=int(input("enter the 10 rupee coin:"))
            tw_coin=int(input("enter the 20 rupee coin:"))
            change=(5*f_coin+10*t_coin+20*tw_coin)-dict['espresso']['price']
            print(f"here is your{change} change")
            print(f"Here is your {name}")
            milk-=dict['espresso']['milk']
            water-=dict['espresso']['water']
            profit+=dict['espresso']['price']
    elif(name=='cappuccino'):
        if((milk<dict['cappuccino']['milk'] and water<dict['cappuccino']['water'])):
            print("sorry,not enough milk or water")
        elif(milk>=dict['cappuccino']['milk'] and water>=dict['cappuccino']['water']):
            print("please insert coin")
            f_coin=int(input("enter the 5 rupee coin:"))
            t_coin=int(input("enter the 10 rupee coin:"))
            tw_coin=int(input("enter the 20 rupee coin:"))
            change=(5*f_coin+10*t_coin+20*tw_coin)-dict['cappuccino']['price']
            print(f"here is your{change} change")
            print(f"Here is your {name}")
            milk-=dict['cappuccino']['milk']
            water-=dict['cappuccino']['water']
            profit+=dict['cappuccino']['price']