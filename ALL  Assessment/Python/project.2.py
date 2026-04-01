user_name=input("enter your name :")
total=0
all_total=0
mam=input("are you mamber of this shop if yes press-> (yes) or press-> (no) :")
buy=int(input("enter how many item you wanted to by :"))
for i in range(buy):
    item_name=input(f"enter your item {i+1} name : ")
    q=int(input("enter your qualntity :"))
    price=int(input("enter price :"))
    total_pri=q*price
    all_total+=total_pri
    if q>5:
        q_dis=(total_pri*5)/100
        total+=total_pri-q_dis
        total_pri=total_pri-q_dis

    print(f"{item_name} total ={total_pri}")

print("total bill :-",total)

if total>2000:
    b_dis=(total*15)/100
    total-=b_dis
elif total>1000:
    b_dis=(total*10)/100
    total-=b_dis
elif total>500:
    b_dis=(total*5)/100
    total-=b_dis

if mam=="yes":
    m_dis=(total*5)/100
    total-=m_dis

gst=(total*18)/100
total+=gst

print(f"finaml total={total}")
print(f"thank you for coming <{user_name}>")
print(f"ALL TOTAL BILL={all_total}")

if mam=="yes":
    print(f"membership discount = {m_dis}")


if total>2000:
    print("parchesing =",b_dis)
elif total>1000:
    print("parchesing =",b_dis)
elif total>500:
    print("parchesing =",b_dis)

print("GST =",gst)

print(f"§§: TOTAL={total} :§§")