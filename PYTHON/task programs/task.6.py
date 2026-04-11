# take 4 number from user and count how many number are positiv and how many numbers are negetiv

p=0
n=0
for i in range(1,5):
    num=int(input(f"enter your {i} number :"))
    if num>0:
        print(f"{num} positiv")
        p+=1
    else:
        print(f"{num} nagtiv")
        n+=1

print(p,)
print(n,)