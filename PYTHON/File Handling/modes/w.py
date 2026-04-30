with open('myfile2.txt','w') as f:
    f.write('hello good mornig\nmustved'.title())
    f.write("\nthis is my first file creation...".title())
print('file created successfully!.'.upper())

with open('username.txt','w') as f:
    for i in range(5):
        name=input(f'enter your name {i+1} :').capitalize()
        f.write(f'{name}\n')
print('name add successfuly.....'.upper())