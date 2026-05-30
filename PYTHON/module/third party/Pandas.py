import pandas as p

data={
    'name':['mustved','aaa','bbb','a','b','c','d'],
    'subject':['python','java','php','a','b','c','d'],
    'id':[1,2,3,4,5,6,7]
}

ok=p.DataFrame(data)
print(ok)
print("--------------------------")
print(ok.head())# ye khali uper ke 5 datad hi nikal ke dega
print("--------------------------")
print(ok.tail())# ye niche ke 5 data ikal ke dega
print("--------------------------")
print(ok.shape)#ye btaye ga kitni row or column hai
print("--------------------------")
print(ok.info())# ye information dega int ke column kitne hai str ke kitne
print("--------------------------")
print(ok.columns)#keys dikhata hai
print("===========================")

doc=dict(ok)
print(doc)

print("+++++++++++++++++++++")
print(ok['id']>4)# ye jo id 4 se jyada hogi vo true or baki ki false btayega

print("--------------------------")
print(ok['name'])#khali name ke liye
print("--------------------------")
print(ok[['name','subject']])# name or subject dono ke liye
print("--------------------------")
print("--------------------------")
lst=list(ok)
print(lst)
print("--------------------------")
lst=list(ok['name'])
print(lst)


# ook=p.read_csv("file.csv")# task 55 run hoga to ye file bane gi
# print(ook)
print("--------------------------")
# index se 
print(ok.loc[1])# index 1 se sara data dikha dega
