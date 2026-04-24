# list ke ander dictionary me add kare
l1=[
    {"product": "Apple", "quantity": 10, "price": 0.5,},
]

l1[0]['total']=l1[0]['quantity']*l1[0]['price']
for i,j in l1[0].items():
    print(i,j)