try:
    num1=int(input('enter our number1 :'))
    num2=int(input("enter your number2 :"))
    ans=num1/num2
    print(ans)
except ValueError:
    print('enter numbers only!!!')
except ZeroDivisionError:
    print(f'{num1} : cannot divide by 0 !!!!')
except:
    print('somthin want wrong...')
