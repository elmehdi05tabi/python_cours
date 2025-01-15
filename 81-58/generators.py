# --------------------
# Generators 
# --------------------
# [1] Generators is a fucntion with "yield" keyword instead of "return"
# [2] it support iteration and return generator iterator by calling "yield"
# [3] generator function can have one or more "yield"
# [4] by using next() it resume from where it called "yield" not from begining
# [5] when called , its not start automatically , its only give you the control
# --------------------------------------------------------------
def myhenerators () :
    yield 1 
    yield 2
    yield 3 
    yield 4 
# print(myhenerators) 

gen = myhenerators()
print(next(gen))
print("bonjour python")
print(next(gen)) 
print("bonjour python")
for i in gen: 
    print(i)

