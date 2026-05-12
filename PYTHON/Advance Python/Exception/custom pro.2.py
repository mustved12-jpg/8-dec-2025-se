class error(Exception):
    pass

try:
    num=int(input("enter number :"))
    if num<18:
        raise error("you are not above 18..")
    else:
        print("{}______welcom____{}")
except error as e:
    print(e)
    
except:
    print("enter only number")
else:
    print("your number =",num)
