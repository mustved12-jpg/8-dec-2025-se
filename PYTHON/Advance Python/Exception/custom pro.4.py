class error(Exception):
    pass
def numbers(num):
    if num<0:
        raise error("enter positiv number only.....")#agar number negetiv huva to Erorr me ye vala massge jayega 
    if num%2==0:
        raise error("even number not accepteble!!")#agar number even huva to Erorr me ye vala massge jayega
    else:
        print(f"welcom your number is {num}")
try:# isme agr function vali Error ko chod ke koi bhi error aye gi to except 2 me jaye ga  
    nu=int(input("enter your number :"))# agar number ke alava kuch bi dalunga to except 2 me jaye ga
    numbers(nu)# agar error aye gi to except 1 me jaye ga 
except error as e:#1
    print(e)
except:#2 ye samjho else ki tra hai if else vala else age koi error ayi agar humne difine kiya hoga to us vale 
    # except me jaye ga varna sab isme to ayega hi difine matlab jese humne excep 1 me kiya hai
    print('enter numbers only...')
else:
    print("good job you are entring into next face......")#agar error nhi aye gi to ye vala ayega 