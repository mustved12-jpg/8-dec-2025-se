quiz={
    1:{'que':'whois prime minister of india ?','ans':'narendra modi'},
    2:{'que':'most populer programing language ?','ans':'python'},
    3:{'que':'most populer cricketer ?','ans':'ms dhoni'}
}

print(quiz[1]['que'])
print(quiz[1]['ans'])
print("___________________")

print("___________________")


r,w=0,0
for i in range(1,len(quiz)+1):
    print(f"({i}){quiz[i]['que']}")
    ans=input(f"{i} enter your ans :").lower()
    if ans==quiz[i]['ans']:
        print("right ans...\n\n")
        r+=1
    else:
        print("wrong ans !!!\n\n")
        w+=1

print("right =",r)
print("wrong =",w)
