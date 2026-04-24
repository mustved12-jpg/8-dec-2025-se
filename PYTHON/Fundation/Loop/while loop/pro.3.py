u_name="mustved"
u_email="mustved@gmail.com"
u_password="1234abcd"
menu="""
                ::menu::
            press ->1 for login
            press ->2 for register
            press ->3 exit
    """

status=True
while status:
    print(menu,)
    ch=int(input("enter your choise :"))
    match ch:
        case 1:
            print("-------------login---------------")
            email=input("enter your email :")
            password=input("enter your password :")
            if u_email==email and u_password==password:
                print(f"welcom <<<<<<<<<{u_name}>>>>>>>>>> ")
            else:
                print("``invalid details!!")
                status=False
        case 2:
            print("-----------register-------------")
            email=input("enter your email :")
            password=input("enter your password :")
            u_email=email
            u_password=password

        case 3:
            print("thank you for coming...")
            status=False 