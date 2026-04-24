#Q 27: Write a function that accepts two strings and checks if one string is an anagram of the other.
name1='mustved'
name2='devmuts'
if len(name1)==len(name2):
    for i in range(len(name2)):
        if name2[i] not in name1:
            f=0
            break
        elif name1[i] not in name2:
            f=0
            break
        else:
            f=1
    if f==1:
        print("anagram".upper())
    else:
        print("not a anagram".title())
else:
    print("not a anagram")
