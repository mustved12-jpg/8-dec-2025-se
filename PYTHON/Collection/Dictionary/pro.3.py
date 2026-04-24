s={'name':'mustved','subject':'python','score':65}

print(s)

print(s.get('name'))
print("___________key and value______________")
for k,v in s.items():
    print(f"{k} = {v}")

print('________________only key_______________')
for k in s.keys():
    print(k)

print('________________value___________________')
for v in s.values():
    print(v)
