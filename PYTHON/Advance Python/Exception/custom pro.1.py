class age(Exception):
    pass
number=int(input("enter your age :"))
if number<18:
    raise age("you are not above 18..")
else:
    print("......walcom....")
