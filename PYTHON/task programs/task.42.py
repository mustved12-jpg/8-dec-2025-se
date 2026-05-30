
# monkey patcihng
class A:
    def my(self):
        return 5
def ok(self):
    return 10
a=A()
print(a.my())
A.my=ok
print(a.my())