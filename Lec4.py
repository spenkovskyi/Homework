"""def alpha(s):
    while True:
       try:
           s.isalpha() == True
       except ValueError:
           print("Try again")
       else:
           print("Row is ok")
           assert s.isalpha()
           return s
s=input("Enter Row\n")
alpha(s)
def func(*args):
    return args
func(1,"strtr",56, False)
print(func(1,"strtr",56, False))
print(type(func(1,"strtr",56, False)))


def fc(*args):

    return args

res = fc(1,4,5,8, 'str ')
r = list(res)
r = sorted(r)
print(r[1])

def f(**kwargs):
    return str(kwargs.get('name'))+' is '+ str(kwargs.get('job'))

print(f(a=1, job='lazy',name="Bob"))
print(f())

"""
import new_package.my_mod
f = new_package.my_mod.func1(1)
print(f)