class kuch_bhi(Exception):
    pass
def ATM(withdrow,balance=5000):#using function defualt argument
    if balance<withdrow:
        raise kuch_bhi("Insufficient balance!!!!")
    else:
        print("withdrow successfuly...")
amount=int(input("enter your amount :"))
try:
    ATM(amount)
except kuch_bhi as e:
    print("ERROR :-",e)
else:
    print(f"{amount}.Rs...")
finally:
    print("thank you for coming....")