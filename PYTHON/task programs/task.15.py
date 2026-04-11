name="immustvedmi"
print(name)
for char in name:
    if char.isnumeric():
        flage=1
    else:
        flage=0
if flage==1:
    print("ok")
else:
    print("no")