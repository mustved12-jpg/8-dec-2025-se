import json
d={'id':1,'name':'mustved','score':67}
print('python data :',d)

with open('json 1.json','w') as f:
    json.dump(d,f,indent=4)#indent se humko har key ke pehle 4 space mil jayega agar hum isko nhi
    # likhenge to ek line me hi aye ga 
print('successfuly file converted!')