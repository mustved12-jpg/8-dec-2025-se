import re

data="hello+my name*is-mustved"
result=re.split(r"[+* -]",data)
print(result)

