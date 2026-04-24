l1=[10,20,[101,102,103,[201,202,203,[301,302,[400],303],204,205],104,105],30,40]
print("print = 10 in list")
print(l1[0])#10
print(l1[1])#20
print("print = 102 & 103 in list")
print(l1[2][1])#102
print(l1[2][2])#103
print(l1[2][5])#105
print("print = 202 & 204 in list")
print(l1[2][3][1])#202
print(l1[2][3][4])#204
print("print = 301 & 303 in list")
print(l1[2][3][3][0])
print(l1[2][3][3][3])
print("print = 400 in list")
print(l1[2][3][3][2][0])

