name="im mustved 65878 782 sdbkjndkj"
print(name)
sume=""
char=""
for chr in name:
    if ord(chr)>=ord("0") and ord(chr)<=ord("9"):
        sume+=chr
    else: 
        char+=chr
print(sume)
print(char)