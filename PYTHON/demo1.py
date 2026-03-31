'''
pro.1

name=input("enter your name :")
score=int(input("enter your score :"))
pri=float(input("enter price :"))

print("datatype :",type(name),type(pri))
print("address of pri =",id(pri))

print("name =",name,"and score is =",score,"and price =",pri)
print(f"name = {name} and score is = {score} and price = {pri}")
print("name = {0} and score is = {2} and price = {1}".format(name,pri,score))

---------------------------------------------------------------------


pro.2
name=input("enter you name :")
age=int(input("enter you age :"))
tex=input("inter your tecnology :")
score=float(input('enter yor score'))

print(f"my name is {name} i am {age} years old.")
print(f"my main technology is {tex},this {tex} technology is most popule and my score is={score}")

print("check",type(name))
from sys import get_int_max_str_digits
------------------------------------------------------------------------

pro.3

user_name=input("enter you name :")
t_sirt,geans,jacket=300,500,2000
print(f"1-tsirt and prince = {t_sirt}")
print(f"2-geans and prince = {geans}")
print(f"3-jacket and prince = {jacket}")

ch=int(input("enter our choise :"))
q=int(input("enter your quintity :"))
if ch>=0 and ch<=4:
    if ch==1:
        print(f"... <{user_name}> you orderd tsirt....")
        print(f"it's price is -> {t_sirt} and quantity {q}.")
        total=t_sirt*q
        if total>=300 and total<=499:
            t_dis=(total*5)/100
            gst=(total*5)/100
            print(f"TOTAL with 5% tsirt discount and  5% GST = {total-t_dis+gst}")

        elif total>=500 and total<=999:
            dis=(total*10)/100
            t_dis=(total*5)/100
            gst=(total*5)/100
            print(f"your total price is = {total} and discount = {dis}")
            print(f"5% tsirt discount = {t_dis} current amount is = {(total-dis)-t_dis} add GST 5% {gst}")
            print("::: TOTAL ~>",total-dis-t_dis+gst)
        elif total>=1000 and total<=1999:
            dis=(total*20)/100
            t_dis=(total*5)/100
            gst=(total*12)/100
            print(f"your total price is = {total} and discount = {dis}")
            print(f"5% tsirt discount = {t_dis} current amount is = {(total-dis)-t_dis} add GST 12% {gst}")
            print("::: TOTAL ~>",total-dis-t_dis+gst)
        elif total>=1999:
            dis=(total*30)/100
            t_dis=(total*5)/100
            gst=(total*12)/100
            print(f"your total price is = {total} and discount = {dis}")
            print(f"5% tsirt discount = {t_dis} current amount is = {(total-dis)-t_dis} add GST 12% {gst}")
            print("::: TOTAL ~>",total-dis-t_dis+gst)

    elif ch==2:
        print(f"... <{user_name}> you orderd geans....")
        print(f"it's price is -> {geans} and quantity {q}.")
        total=geans*q
        if total>=300 and total<=499:
            g_dis=(total*8)/100
            gst=(total*5)/100
            print(f"TOTAL with 8% geans discount and  5% GST = {total-t_dis+gst}")

        elif total>=500 and total<=999:
            dis=(total*10)/100
            g_dis=(total*8)/100
            gst=(total*5)/100
            print(f"your total price is = {total} and discount = {dis}")
            print(f"8% geans discount = {g_dis} current amount is = {(total-dis)-g_dis} add GST 5% {gst}")
            print("::: TOTAL ~>",total-dis-g_dis+gst)
        elif total>=1000 and total<=1999:
            dis=(total*20)/100
            g_dis=(total*8)/100
            gst=(total*12)/100
            print(f"your total price is = {total} and discount = {dis}")
            print(f"8% geans discount = {g_dis} current amount is = {(total-dis)-g_dis} add GST 12% {gst}")
            print("::: TOTAL ~>",total-dis-g_dis+gst)
        elif total>=1999:
            dis=(total*30)/100
            g_dis=(total*8)/100
            gst=(total*12)/100
            print(f"your total price is = {total} and discount = {dis}")
            print(f"8% geans discount = {g_dis} current amount is = {(total-dis)-g_dis} add GST 12% {gst}")
            print("::: TOTAL ~>",total-dis-g_dis+gst)

    elif ch==3:
        print(f"... <{user_name}> you orderd jacket....")
        print(f"it's price is -> {jacket} and quantity {q}.")
        total=jacket*q
        if total>=300 and total<=499:
            j_dis=(total*12)/100
            gst=(total*5)/100
            print(f"TOTAL with 12% jacket discount and  5% GST = {total-j_dis+gst}")

        elif total>=500 and total<=999:
            dis=(total*10)/100
            j_dis=(total*12)/100
            gst=(total*5)/100
            print(f"your total price is = {total} and discount = {dis}")
            print(f"12% jacket discount = {j_dis} current amount is = {(total-dis)-j_dis} add GST 12% {gst}")
            print("::: TOTAL ~>",total-dis-j_dis+gst)
        elif total>=1000 and total<=1999:
            dis=(total*20)/100
            j_dis=(total*12)/100
            gst=(total*12)/100
            print(f"your total price is = {total} and discount = {dis}")
            print(f"12% jacket discount = {j_dis} current amount is = {(total-dis)-j_dis} add GST 12% {gst}")
            print("::: TOTAL ~>",total-dis-j_dis+gst)
        elif total>=1999:
            dis=(total*30)/100
            j_dis=(total*12)/100
            gst=(total*12)/100
            print(f"your total price is = {total} and discount = {dis}")
            print(f"12% jacket discount = {j_dis} current amount is = {(total-dis)-j_dis} add GST 12% {gst}")
            print("::: TOTAL ~>",total-dis-j_dis+gst)
        
    else:
        print(":::wrong choice:::")
---------------------------------------------------------------------
'''

print("hello",end=" ")
print("mustved")