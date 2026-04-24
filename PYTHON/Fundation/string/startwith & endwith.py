name="http://www.gmail.com"

print(name.startswith("http"))#True

if name.startswith("http://") or name.startswith("https://"):
    if name.endswith(".com") or name.endswith(".in") or name.endswith(".co"):
        print("...VALID URL...")
    else:
        print("URL end dosenot match!!")
else:
    print("invalid URL!!!!")
    