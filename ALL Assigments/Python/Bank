user_info={}
bank_manegment={}
l1=[]#saving history
print("\n\t\t\t>>>>>>>>>>>>>>>>>>>>>>:BANK MANAGMENT SYSTEM:<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
acc_num=1000
balance=5000
while 1:
    role=int(input("""\t\t      * * * * * * * * * * * * * * * * * *
                      *      :menu:                     *
                      *  press 1 for creat account      *
                      *  press 2 for login              *
                      *  press 3 for exit               *
                      * * * * * * * * * * * * * * * * * *
    enter choice :""".upper()))
    if role<=3 and role>=1:
        if role==1:
            while 1:        
                sub_d={}
                user_email=input("\nenter your email :".upper())
                if "@" in user_email and "." in user_email:
                    if user_email in user_info:
                        print("\nthis name alredy exist!!".upper())
                        continue
                    else:
                        pass
                else:
                    print("\n\t\tnot correct email!!!")
                    continue
                user_pas=int(input("enter your password :".upper()))
                if user_pas>9999999 and user_pas<999999999999:
                    pass
                else:
                    print("\nyour possword must bitween 8 to 12 charecter !")
                    continue
                user_name=input("\nenter your name :".upper())
                sub_d['name']=user_name
                sub_d['password']=user_pas
                acc_num+=1
                sub_d['account number']=acc_num
                print("\n\t\t------:account successfully created:---------".upper())
                print("____________________________________________________________\n\n")
                user_info[user_email]=sub_d
                break
        elif role==2:
            print("--------------------:login:-----------------------\n")
            user_email=input("enter your email :".upper())
            user_pas=int(input("enetr your password :".upper()))
            if user_email in user_info and user_pas==user_info[user_email]['password']:
                print(f"---------------welcom {user_info[user_email]['name']}--------------------")
                while 1:
                    acount=user_info[user_email]['account number']
                    sub_d={}
                    bal=int(input("""
                                        :menu:
                                    press 1 for diposit
                                    press 2 for withdrol
                                    press 3 for view
                                    press 4 for exit
                    
                    enter your choice :""".upper()))
                    if bal==1:
                        print("=============:deposit:===========")
                        d_amount=int(input("\nenter your amount :".upper()))
                        balance+=d_amount
                        sub_d['balence']=balance
                        l1.extend(['diposit',d_amount])
                        sub_d['transection']=l1
                        bank_manegment[acount]=sub_d
                    elif bal==2:
                        print("\n=============:withdrow:===========")
                        w_amount=int(input("enter your amount :".upper()))
                        balance-=w_amount
                        sub_d['balence']=balance
                        l1.extend(['withdrow',w_amount])
                        sub_d['transection']=l1
                        bank_manegment[acount]=sub_d
                    elif bal==3:
                        print("------------view details------------\n")
                        for i in bank_manegment:
                            if i==user_info[user_email]['account number']:
                                print("user name :".upper(),user_info[user_email]['name'],end=" | ")
                                print("account number :".upper(),i,end=" | ")
                                print("total balance :".upper(),balance,end=" |\n")
                                print("\n==========================:>transcations<:==============================\n".upper())
                            for j in bank_manegment[i]:
                                ok=0
                                for p in l1:
                                    if ok==0:
                                        print(p,end=" : ")
                                        ok+=1
                                    elif ok==1:
                                        print(p,end=" | ")
                                        ok-=1     
                                break
                            break
                        print("\n------------------------------------------------\n")                     
                    else:
                        break
            else:
                print("not exists....".title())
                print("creat account first..".upper())
        else:
            break
    else:
        print("\n\n\t\t\twrong number!!!!!\n\n".upper())