name1='madam'
name2="madam"

if name1==name2[::-1]:
    print(" string is palindrom")
else:
    print(" string is not palindrom")



s1=len(name1)
s2=len(name2)
for i in range(s1 or s2):
    if name1[i]==name2[s2-1]:
        f=1
    else:
        f=0
if f==1:
    print("palindrom")
else:
    print("not palindrom")