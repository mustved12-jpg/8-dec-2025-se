student={
    'tel1':{'name':'mustved','score':76,'sub':'python'},
    'tel2':{'name':'juned','score':67,'sub':'java'},
    'tel3':{'name':'boss','score':90,'sub':'php'},
}
for i in range(1,len(student)+1):
    print(student[f'tel{i}']['name'],student[f'tel{i}']['sub'],student[f'tel{i}']['score'])