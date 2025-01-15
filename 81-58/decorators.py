# ------------------------------
# ---Decorators---
# [1] sometime called meta programing
# [2] everthing in python is object even functions 
# [3] decorator take a fucntion and add some functionality and return it 
# [4] decorator wrap other function and enhance their behaviour
# [5] decorator is higher order function (fucntion accept function as parametr)
# ------------------------------
def mondecor (func) :  #decorators 
    def nestedfun() :  
        print("befor") # message from decorators 
        func() #exuxted function
        print("after") # message from decorator 
    return nestedfun
@mondecor
def dit_bonjour () :
    print("bonjour dans cette matin")

# decor = mondecor(dit_bonjour)
# decor()
dit_bonjour()
print("#"*50)
@mondecor
def say_hello () : 
    print("hello from this morning : ")
say_hello()