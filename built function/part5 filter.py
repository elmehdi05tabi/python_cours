# --------------------------------------------
# -- built in fucntion  => filter --
# --------------------------------------------
# [1] filter take a function + iterator 
# [2] filter run a function on every elment 
# [3] the function can be pre-defined function or labda function 
# [4]  filter out all elements for which the function return true 
# [5] the function need to return boolean value 
# --------------------------------------------
#  Exampe 1  :
def chekNumber (num) : 
    # if num == 0  : 
    #     return True 
    return num > 10 
myNumber = [0,10 ,9,5,0,14,96,0,33] 

mytcheck = filter(chekNumber ,myNumber )
for number in mytcheck : 
    print(number)
print("#"*50)
#  Exemple 2 : 
def checkText (name) :
    if name.startswith("A") : 
        return name 
mypersone = ["Ahmed","Elmehdi","Anoir","Akram","Osama"]
for p in filter(checkText , mypersone) : 
    print(p)

#  Example 3 : for lambda function 

Not = [10.5,9,18,63,87,6]
for n  in filter(lambda note :note > 10 ,Not) :
    print(n)