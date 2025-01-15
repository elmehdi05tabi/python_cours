# ----------------------------------
# ---- function => lamba ----
# ---- anonymos fuction ----
# ----------------------------------
# [1] it has no name 
# [2] you can call it inline whithout definig it 
# [3] you can use it in return data from another function 
# [4] lamba used for simple functions and def hanle the large tasks
# [5] lambad is one single expression not block of code 
# [6] lamba type is function 
# ----------------------------------

def say_hello(name,age) :
    return f"hello {name} your age is {age}"
hello = lambda name ,age : f"hello {name} your age is {age}"
print(say_hello("elmehdi",12))
print(hello("tabi",19))