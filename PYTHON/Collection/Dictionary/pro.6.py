pro={}
menu="""\n
                        :menu:
                    press 1 for meneger
                    press 2 for costomenr
                    press 3 for exit
\n""".upper()

while 1:
    print(menu)
    role=int(input("enter your name :".upper()))
    if role==1:
        while 1:  
            print("\n\t\t~~~~~~~~~~~~~~~~~~~~:welcom meneger:~~~~~~~~~~~~~~~~~~~~\n".upper())
            m_menu="""
                                ::menu::
                            press 1 for adding 
                            press 2 for removing 
                            press 3 for seeing
                            press 4 for exit
            """.upper()
            print(m_menu)
            m_ch=int(input("enter your choice :".upper()))
            if m_ch==1:
                print("\n\t\t-----------------------------:add:--------------------------------\n")
                while 1:
                    sub={}
                    pro_name=input("enter your product name :".title())
                    pro_pri=int(input(f"enter your {pro_name.upper()} price :".title()))
                    pro_q=int(input("enter your product quantity :".title()))
                    pro_dis=float(input("enter discount :".title()))
    #               adding on sub 
                    sub['price']=pro_pri
                    sub['quantity']=pro_q
                    sub['discount']=pro_dis
                    # adding sub into main pro
                    pro[pro_name]=sub

                    more=input("""
                                    do you wanted to add more product
                                    press -> (y) for yes
                                    press -> (n) for no
                    enter :""".upper()).upper()
                    if more=="Y":
                        continue
                    else:
                        break

            elif m_ch==2:
                print("\n\n\t\t-----------------------:remove:------------------------------\n".upper())
                ch=input("enter wat you wanted to removing eliment : ".upper())
                pass
            elif m_ch==3:
                print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                for i in pro:
                    print(f"{i}:- price : RS.{pro[i]['price']} | quantity : {pro[i]['quantity']} | discount : {pro[i]['discount']}%")
                    print("_______________________________________________________\n\n")
            else:
                break

    elif role==2:
        total=0
        all_total=0
        discount_total=0
        print("\t\t<><><><><><><><><><>:welcom:<><><><><><><><><><>".upper())
        while 1:
            print("""\n\t________________>menu<___________________""".upper())
            j=1
            for i in pro:
                print(f"\t\tpress -> {j} for {i}")
                j+=1
            j=1
            u_ch=int(input("\nenter your choice :".upper()))
            for i in pro:
                if u_ch==j:
                    print(f"your choice is {i}\n".title())
                    print(f"\tit's price = RS.{pro[i]['price']}")
                    print(f"\n\n-------if you by more then 5 quantity you will gate {pro[i]["discount"]}% discount.----------\n".upper())
                    q=int(input("enter your quantity:".upper()))
                    total=q*pro[i]['price']
                    discount=0
                    if q>=5:
                        discount=(total*pro[i]['discount'])/100
                    break
                else:
                    j+=1
            all_total+=total
            discount_total+=(total-discount)
            print(f"your total : {total} and discount : {discount}% = RS.{total-discount}")
            print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            more_by=input("\ndo you wanted to by more items press (y) or press (n) :".title()).upper()
            if more_by=="Y":
                continue
            else:
                print("\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                print("thank you for comming".upper())
                print(f"your all total bil is = RS.{all_total} and with discount you have to pay = RS.{discount_total}".title())
                break
        break
         
    else:
        break