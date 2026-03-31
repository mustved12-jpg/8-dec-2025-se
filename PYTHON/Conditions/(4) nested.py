'''mark=int(input("enter your mark :"))

if mark>=100 and mark<0:
    if mark>=70:
        print("A gread")
    elif mark<70 and mark>=60:
        print("B gread")
    elif mark<60 and mark>=50:
        print("C gread")
    elif mark<50 and mark>=40:
        print("D gread")
    else:
        print("fail")
else:
    print("invalid input:")

-------------------------------------------------------------------------------------------------------
'''
a,b,c=10,20,30
if a>=b:
    if a>=c:
        print(f"{a} is greter number!")
    else:
        print(f"{c} is grete number!")
else:
    if b>=c:
        print(f"{b} is greter number!")
    else:
        print(f"{c} is greter number!")