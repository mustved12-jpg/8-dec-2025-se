# save only 4 charecter from list

l1=["java","mustved12","php",87,"python","android","fluter",]
l2=[]
l3=[]
# witout list comprehension

for i in l1:
    if type(i)==str and i.isalpha():
        l2.append(i[0:4])
    else:
        l3.append(i)
print(l2)
print(l3)

# with list comprehension
l5=[]
l4=[i[:4] if type(i)==str and i.isalpha() else l5.append(i) for i in l1]
# agar hum list comprehension mai kisi dusri list me appned karenge to vo dusri list me apend to karega but
# is list me  none likhe le sav kare ga 
print("l4 =",l4)
print("l5 =",l5)