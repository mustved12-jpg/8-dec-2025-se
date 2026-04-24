student={'name':'mustved','subject':'python','score':76}
print(student)
print(student['name'])
print(student['subject'])
print(student['score'])
#print(student['city'])  KeyError: 'city'
# is me agar key city nhi hogi to erorr ayegi
#___________________________________________________


#method 2

print(student.get('name'))
print(student.get('subject'),end=" = ")
print(student.get('score'))
print(student.get('city'))# ye nhi hogi to erorr nhi none dikhaye ga 
print(student.get('city','ahmendabad'))# ab ye none nhi dikhaye ga ab ye ahmendabad dikhayega 

