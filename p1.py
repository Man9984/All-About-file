################ Python Program #################
# BLL

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

#PL

a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))

sum = add(a,b)
sub = sub(a,b)
mul = mul(a,b)
div = div(a,b)
print(sum,sub,mul,div)