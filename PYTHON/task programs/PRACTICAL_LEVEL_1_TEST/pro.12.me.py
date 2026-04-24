def vowel():
    d={'vowels':{},'com':{}}
    name=input("enter your name :".title())
    for i in name:
        if i=='o' or i=='u' or i=='i' or i=='e' or i=='a':
            if i not in d['vowels']:
                d['vowels'][i]=1
            else:
                d['vowels'][i]+=1
        else:
            if i not in d['com']:
                d['com'][i]=1
            else:
                d['com'][i]+=1
    return d
print(vowel())