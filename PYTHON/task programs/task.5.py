# take 5 numbers and print number is positiv or nagetiv

for i in range(6):
    number=int(input(f"enter your {i+1} number :"))
    if number>0:
        print(f"{number} is positive ")
    else:
        print(f"{number} is nagetiv")