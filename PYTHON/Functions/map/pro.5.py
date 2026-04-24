# agar me mai map function mai codition ke hisab se ko value ko save karta hu to true vali
# to save hogi but false vali me none save hoga agae humko none save hi kana hai to hum map 
# nhi filter function ka use karenge 

l1=['java','python','php','ai','flutter']
def myfun(name):
    if len(name)>4:
        return name

l2=list(map(myfun,l1))
print(f"{l1}\n{l2}")