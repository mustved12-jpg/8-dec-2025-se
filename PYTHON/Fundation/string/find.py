name='mustved@gmai.com'

print(name)
print(name.find("@"))

if "@" in name and "." in name:
    print("valid email.")
else:
    print("invalid email!")
