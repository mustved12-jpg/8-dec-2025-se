li=[]
for i in range(3):
    day=input("enter your day :")
    tam=float(input("enter temp:"))
    if tam>=25:
        li.extend([day,tam])
p=0
print(li)
print(len(li))
for j in li:
    if p==len(li):
        break
    print(f"{li[p]} temp ",end="")
    p+=1
    print(li[p])
    p+=1