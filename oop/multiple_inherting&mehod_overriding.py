# ---------------------------------------------------------------
# -- object oriented programming => Multiple Inhertance 
# ---------------------------------------------------------------

class BaseOne : 
    def __init__(self) : 
       print("base one")
    def fun_one (self) : 
        print("one")

class BaseTwo : 
    def __init__(self) : 
       print("base two")
    def fun_two (self) : 
        print("two")

class Derive(BaseTwo , BaseOne)  : 
    pass 
var = Derive()
print(Derive.mro()) #! mro => method reselution order 
print(var.fun_one)
print(var.fun_two)
var.fun_one()
var.fun_two()




class base :
    pass 
class derivone(base) : 
    pass
class derivtwo (derivone) : 
    pass 