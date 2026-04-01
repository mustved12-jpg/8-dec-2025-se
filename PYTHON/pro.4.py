p=0
n=0
for i in range(1,5):
    num=int(input(f"enter your {i} number :"))
    if num>0:
        print(f"{num} positiv")
        num+=p
    else:
        print(f"{num} nagtiv")
        num-=n

print(p,)
print(n,)