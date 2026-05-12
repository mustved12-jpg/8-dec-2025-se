import os
os.chdir(os.getcwd()+"\\exception")
try:
    os.mkdir('my folder')
except:# exception huva to ye aye ga
    print('somthin want wrong!!!')
else:# ye agar exception nhi hoga tab aye ga 
    print("folder created successfuly~~~")
finally:
    print("@@@@@ thank you for coming @@@@@")# ye har bar aye ga chahe exception ho ya na ho 