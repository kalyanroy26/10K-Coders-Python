num_1 = 10
num_2 = 2

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def exp(a,b):
    return a**b

def floordiv(a,b):
    return a//b

def expdiv(a,b):
    return a%b

print("add:",add(num_1,num_2))
print("sub:",sub(num_1,num_2))
print("mul:",mul(num_1,num_2))
print("div:",div(num_1,num_2))
print("exp:",exp(num_1,num_2))
print("floordiv:",floordiv(num_1,num_2))
print("expdiv:",expdiv(num_1,num_2))

print('\n')
print("Lamda functions ")

# LAMBA FUNCTIONS

add_l = lambda a,b : a+b
sub_l = lambda a,b : a-b
mul_l = lambda a,b : a*b
div_l = lambda a,b : a/b
exp_l = lambda a,b : a**b
floordiv_l = lambda a,b : a//b
expdiv_l = lambda a,b : a%b



print("add: ",add_l(num_1,num_2))
print("sub: ",sub_l(num_1,num_2))
print("mul: ",mul_l(num_1,num_2))
print("div: ",div_l(num_1,num_2))
print("exp: ",exp_l(num_1,num_2))
print("floordiv: ",floordiv_l(num_1,num_2))
print("expdiv: ",expdiv_l(num_1,num_2))




