import random
print("+++++++++++§game§++++++++++++")
computer=random.randint(1,100)
status=True
i=1
print(f"you have only 7 chanses to gess the number..")
while status:
    if i>=1 and i<=6:
        print(f"..|{i}|-> chanse")
    if i==7:
        print("!!!-last chanse thik hard- <o_o!>")
    user=int(input("\nenter your number :"))
    if user > computer:
        print("\n(((((gess lower number..)))))\n")
        if i==4:
            if computer >=5 and computer<=95:
                print("--------------------------------------")
                print(f"hint: bitween {computer+5} to {computer-5}")
                print("--------------------------------------\n")
            elif computer>95:
                print("--------------------------------------")
                print(f"hint: bitween 90 to 100")
                print("--------------------------------------\n")
            elif computer<5:
                print("--------------------------------------")
                print(f"hint: bitween 0 to 10")
                print("--------------------------------------\n")
        if i==7:
            print("your chance is over")
            print("`*v*`")
            status=False
        i+=1
    elif user < computer:
        print("\n((((gess upper number...)))))\n")
        if i==4:
            if computer >=5 and computer<=95:
                print(f"hint: bitween {computer+5} to {computer-5}")
            elif computer>95:
                print(f"hint: bitween 90 to 100")
            elif computer<5:
                print(f"hint: bitween 0 to 10")
        if i==7:
            print("your chance is over")
            print("`*v*`")
            status=False
        i+=1
    else:
        if i==1:
            print("```fastes in the world~~~~")
        print("god jobe")
        status=False
        