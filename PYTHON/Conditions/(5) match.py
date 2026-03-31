'''day=int(input("enter your day :"))

match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thusday")
    case 5:
        print("friday")
    case 6:
        print("surterday")
    case 7:
        print("sunday")
    case _:
        print("invalud day!!")
---------------------------------------------------------------------
   
menu="""                  MENU:
        press -> 1 for playing game.
        press -> 2 for pause game.
        press -> 3 for exit game.
        """
print(menu,)
ch=int(input("enter your choice :"))

match ch:
    case 1 :
        print("```walcom to the super mario;;;;")
    case 2:
        print("pause game!!!")
    case 3:
        print("....thank you for using this app....")
    case _:
        print("invalid input!!!")

---------------------------------------------------------------------
'''

number=int(input("enter your number :"))

print(number,)

match number:
    case number if number>0:
        print(f"{number} positiv number.")
    case number if number<0:
        print(f"{number} nagetiv number.")
    case _:
        print("0 number")