li=[]
for i in range(6):
    day=input("enter your day :")
    tam=float(input("enter temp:"))
    if tam>=25:
        re= f"{day} temp is{tam}"
        li.append(re)

for i in li:
    print(i)