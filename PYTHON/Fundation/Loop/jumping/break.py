# ye 5 bar to chalega par agra iske bich me koi negetiv number ayega to ye band ho jayega
for i in range(1,6):
    num=int(input("enter your number :"))
    if num<=0:
        break
print("---------------------------------")
# using of while loop 
# ye jab tak negetiv number nhi aye ga tab tak chalega
status=True
while status:
    num=int(input("enter your number :"))
    if num<=0:
        break