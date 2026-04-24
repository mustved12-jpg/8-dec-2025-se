d={
    'vadapaos':{'veg vadapao':{'price':100,'discount':5},'non veg vadapao':{'price':80,'discount':8}},
    'itl is':{'veg itli':{'price':120,'discount':7},'non veg itli':{'price':150,'discount':8}}
}


for k in d:
    for v in d[k]:
        print(v)
"""
output:
        veg vadapao
        non veg vadapao
        veg itli
        non veg itli
"""
for k in d:
    for v in d[k]:
        for j in d[k][v]:
            print(j)

"""
outlut:
        price
        discount
        price
        discount
        price
        discount
        price
        discount
        """
