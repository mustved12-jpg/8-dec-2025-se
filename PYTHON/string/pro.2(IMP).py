# convert upper into lower and lower into upper
name="pYThOn"
name2=""
for chr in name:
    if chr.isupper():
        name2+=chr.lower()
    else:
        name2+=chr.upper()

print(name)
print(name2)