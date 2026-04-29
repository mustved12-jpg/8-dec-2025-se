"""Q  68: Generate Random Password
Write a function generate_password(length) that accepts a length as an argument and returns 
a randomly generated password of that length consisting of uppercase letters, lowercase letters, and digits.

"""

import random
def generate_password(length):
        
    n=''
    for i in range(length):
        up=random.randint(65,90)
        lo=random.randint(97,122)
        nu=random.randint(0,9)
        l1=['up','lo','nu']
        pas=random.choice(l1)
        if pas=='up':
            n+=chr(up)
        elif pas=="lo":
            n+=chr(lo)
        elif pas=='nu':
            n+=str(nu)    
    return n
print(generate_password(8))