#Q 44: Write a function that accepts two strings and returns the common characters between them.
name1='hello mustved'
name2='boss hello'
comun=""
for i in name2:
    if i==" ":
        continue
    if i in name1:
        comun+=i
    else:
        pass
print(comun)
