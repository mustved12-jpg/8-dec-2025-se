"""Q  101: Update Dictionary Values Based on Another Dictionary
Write a function update_dict(d1, d2) that accepts two dictionaries. 
It should update the values of d1 with the values from d2 where the keys match. 
If a key from d2 does not exist in d1, it should be added.

"""
d1={1:10,2:20,3:30}
d2={2:40,5:100,4:80,3:"mustved",1:100}
def update_dict(d1, d2):
    for k,v in d2.items():
        if k not in d1:
            d1[k]=v
        else:
            d1[k]=v
    return d1
print(update_dict(d1,d2))        