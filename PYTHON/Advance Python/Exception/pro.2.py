try:
    num1=int(input('enter our number1 :'))
    num2=int(input("enter your number2 :"))
    ans=num1+num2
    print(ans)
except:
    print('invalid input!!!')
    print('enter number only...')

try:
    print(ans)# agar uper exception nhi aya to isme bhi nhi aye ga agar aya to isme 
except:#mene pass kra hum to kuch bhi nhi aye ga 
    pass